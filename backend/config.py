class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret'
    MONGODB_SETTINGS = {
        'host': 'mongodb://root:examplepassword@192.168.10.61:27019/my_notes_2?authSource=admin'
    }