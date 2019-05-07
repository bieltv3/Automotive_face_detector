import cv2
import time
import numpy as np


def landmarks_img(frame, landmarks, bb, face_size):

    if frame is not None:
        if landmarks is not None:
            # Hard code for the landmarks
            for i, (x, y) in enumerate(landmarks):

                # Small 5 shape landmakrs
                #if i in [36, 39, 45, 42, 33]:

                    # Affine transformation
                #    if i in [36, 45, 33]:
                        #cv2.circle(frame, (x, y), 8, (255, 255, 255), -1)

                 #   cv2.circle(frame, (x, y), 5, (255, 0, 255), -1)
                #else:
                cv2.circle(frame, (x, y), 5, (192, 162, 103), -1)

        if bb is not None:
            frame = frame[bb.top() - 10:bb.bottom() + 30, bb.left() - 10:bb.right() + 10]
            frame = cv2.resize(np.uint8(frame), (face_size, face_size))

    return frame


def compute_fps(num_frames, start):
    end = time.time()
    fps = num_frames / (end - start)
    return fps, end


def demo_fps(camera, frame, fps):
    cv2.putText(frame, '{0:.1f} FPS'.format(fps), (100, camera.getDim()[1] - 100),
                cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))

    return frame
