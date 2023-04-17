import tensorflowjs as tfjs
import keras

model = keras.models.load_model('models/tar_net.keras')
tfjs.converters.save_keras_model(model, 'tfjs_tar')