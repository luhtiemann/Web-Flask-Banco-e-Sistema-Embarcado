from flask import Flask, render_template, session, g
from controllers.admin_controller import admin
from controllers.auth_controller import auth
from flask_login import LoginManager
from datetime import datetime
from models import mqtt_client, topic_subscribe ,Dispenser,Pote,Conta
from models import Dispenser,Pote
from apscheduler.schedulers.background import BackgroundScheduler
from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")

    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    mqtt_client.init_app(app)
    db.init_app(app)
    scheduler = BackgroundScheduler()

    pote_value = None
    reservatorio_value = None

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Connection failed with error code", rc)

    def temp_pote(client, userdata, message):
        global pote_value
        pote_value = float(message.payload.decode("utf-8"))
        print("pote:", pote_value)

    def temp_reservatorio(client, userdata, message):
        global reservatorio_value
        reservatorio_value = float(message.payload.decode("utf-8"))
        print("reservatorio:", reservatorio_value)
    

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            for topic in topic_subscribe:   
                mqtt_client.subscribe(topic) # subscribe topic
        else:
            print('Bad connection. Code:', rc)
    def check_conditions():
        global pote_value, reservatorio_value
        if pote_value is not None and reservatorio_value is not None:
            if pote_value < 500 and reservatorio_value > 500:
                print("Condição satisfeita. Publicando mensagem para acionar o servo.")
                mqtt_client.publish("coleguinhas/servo", 1)

            pote = Pote.query.all()
            datetime_obj = datetime.now()
            nova_leitura_pote = Pote(peso=pote_value, date_time=datetime_obj)
            db.session.add(nova_leitura_pote)

            dispenser = Dispenser.query.all()
            datetime_obj = datetime.now()
            nova_leitura_dispenser = Dispenser(value=pote_value, date_time=datetime_obj)
            db.session.add(nova_leitura_dispenser)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import Conta

    @login_manager.user_loader
    def load_user(conta_id):
        # since the conta_id is just the primary key of our conta table, use it in the query for the conta
        return Conta.query.get(int(conta_id))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')
    

    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app



#parte do joao verificar login e tipo de usuario