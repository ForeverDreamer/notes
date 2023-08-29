from constants.share import PIXEL_ASPECT, FRAME_RATE
from utils.py.date import now


class CameraUtil:

    def __init__(self, engine):
        self._engine = engine

    def add_one(self, conf):
        pass

    def add_many(self, cameras):
        statements = ['//cameraUtil.add_many']
        for conf in cameras:
            keyframes = conf['keyframes']
            kf_pot = keyframes['Point of Interest']
            kf_pos = keyframes['pos']
            kf_zoom = keyframes['Zoom']
            statements += [
                f'var cameraLayer = mainComp.layers.addCamera("{conf["name"]}", {conf["centerPoint"]});',
                f'cameraLayer("Transform")("Position").setValue({conf["pos"]});',
                f'cameraLayer("Camera Options")("Zoom").setValue({conf["Zoom"]});',
                f'cameraLayer("Camera Options")("Focus Distance").setValue({conf["Focus Distance"]});',
                f'cameraLayer("Camera Options")("Aperture").setValue({conf["Aperture"]});',
                f'cameraLayer("Transform")("Point of Interest").setValuesAtTimes({kf_pot[0]}, {kf_pot[1]});',
                f'cameraLayer("Transform")("Position").setValuesAtTimes({kf_pos[0]}, {kf_pos[1]});',
                f'cameraLayer("Camera Options")("Zoom").setValuesAtTimes({kf_zoom[0]}, {kf_zoom[1]});',
                f'cameraLayer.moveBefore(bgLayer);',
            ]
        # return self._engine.execute('CameraUtil.add_many', statements)
        statements.append('\n')
        return statements
