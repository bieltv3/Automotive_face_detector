from utils import haar_face_detection
from utils import alignDlib_face_detecion
from threading import Thread


# Runs captures until a face is detected
class CameraFaceDetector(Thread):

    def __init__(self, face_camera, face_size):
        Thread.__init__(self)

        self.face_camera = face_camera
        self.face_size = face_size

        # Every face camera has a haar face detector thread
        self.detector_thread = alignDlib_face_detecion.Detector()
        self.detector_thread.start()

        # Variable to stop the camera thread if needed
        self.stopThread = False

    # Main thread method
    def run(self):

        # Assume no face detected when camera is first up
        self.face_camera.setFace(None)

        while True:
            if not self.stopThread:

                # Get the frame
                frame = self.face_camera.captureFrame()

                if frame is not None:
                    # Detect if there is a face in the frame with haar service
                    self.detector_thread.detect_face(frame)

                    # Set the face of the detected face (with the dimensions specified) - even if it is None
                    self.face_camera.setFace(self.detector_thread.get_face(self.face_size, self.face_size))

            # End the thread and close the camera
            else:
                self.face_camera.close()
                return

    # State variable for stopping face detector service
    def stop(self):
        # Stop the service for the detector
        self.detector_thread.stop()

        # Stop this face_detector thread
        self.stopThread = True

