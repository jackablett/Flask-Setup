import app.config as config
from app import app

if __name__ == "__main__":
    @app.context_processor
    def globals():
        return {
            "SITE_NAME": config.SITE_NAME
        }
    
    app.run(debug=config.DEBUG, port=config.PORT, host=config.HOST)