from ultralytics import YOLO
import cv2
import os
# import winsound
import numpy as np

# Model Paths
model_path = os.path.join('Casino-live', 'models', 'v8.pt')

# YOLO Model Instantiation
model = YOLO(model_path)

def process_img(frame, rows, cols):
    cv2.resize(frame, (640,360))
    crop_width = int(frame.shape[1])  # 81% of the width
    crop_height = frame.shape[0]  # Full height
    crop_x = int(0.1 * frame.shape[1])  # 9% offset from the left
    crop_x2 = int(0.40 * frame.shape[1]) # 20% offset from the right
    crop_y = int(0.04 * frame.shape[1])  # 9% offset from the top
    crop_y2 = int(0.09 * frame.shape[1])  # 9% offset from the bottom
    cropped_img = frame[crop_y:crop_height-crop_y2, crop_x:(crop_width-crop_x2)]

    tile_width = int(cropped_img.shape[1] / cols)
    tile_height = int(cropped_img.shape[0] / rows)
    return tile_height, tile_width, cropped_img

# def preds(url):
#     # Model Paths
#     model_path = os.path.join('Casino-live', 'models', 'v2.pt')
    
#     # Threshold for label detection
#     detection_threshold = 0.9

#     # YOLO Model Instantiation
#     model = YOLO(model_path)
#     counter = 0
#     counter_dict = {}
#     rows = 4
#     cols = 2
#     tile_height, tile_width, cropped_img = process_img(cv2.imread(url), rows, cols)

#     for j in range(cols):
#         if counter == 9:
#             break
#         for i in range(rows):
#             counter += 1
#             tile = cropped_img[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width]
#             tile = cv2.resize(tile, (640,360))
#             results = model(tile)[0]

#             if counter == 1:
#                 tile1 = tile
#                 counter_dict[counter] = tile1
#             elif counter == 2:
#                 tile2 = tile
#                 counter_dict[counter] = tile2
#             elif counter == 3:
#                 tile3 = tile
#                 counter_dict[counter] = tile3
#             elif counter == 4:
#                 tile4 = tile
#                 counter_dict[counter] = tile4
#             elif counter == 5:
#                 tile5 = tile
#                 counter_dict[counter] = tile5
#             elif counter == 6:
#                 tile6 = tile
#                 counter_dict[counter] = tile6
#             elif counter == 7:
#                 tile7 = tile
#                 counter_dict[counter] = tile7                    
#             elif counter == 8:
#                 tile8 = tile
#                 counter_dict[counter] = tile8   
            
#             print(len(results.boxes.data.tolist()))
#             for result in results:
#                 detections = []
#                 for r in result.boxes.data.tolist():
#                     print(r)
#                     x1, y1, x2, y2, score, class_id = r
#                     x1 = int(x1)
#                     x2 = int(x2)
#                     y1 = int(y1)
#                     y2 = int(y2)
#                     class_id = int(class_id)
#                     if score > detection_threshold:
#                         detections.append([x1, y1, x2, y2, score])

#             for i in range(len(counter_dict)):
#                 frame_text = f'Table {i+1}'
#                 cv2.imshow(frame_text, counter_dict[i+1])
                
#             if (cv2.waitKey(1)):
#                 pass

def preds(url, coords, t_preds, t_counter):
    # print(f'initial: coords: {coords}, t_preds: {t_preds}, t_counter: {t_counter}')
    table = 0
    tolerance = 0.1
    rows, cols = 4, 2
    tile_height, tile_width, cropped_img = process_img(cv2.imread(url), rows, cols)

    # Loop through each tile (8 tile images)
    for i in range(rows):
        if table == 8:
            break
        for j in range(cols):
            table += 1

            # Create Predictions on a tile
            tile = cropped_img[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width]
            tile = cv2.resize(tile, (640,360))
            results = model(tile, verbose=False, max_det=2, imgsz=(1920, 1088))[0] 
            temp_coords = {}
            temp_preds = {}

            # Ensure there is 2 predictions present in a tile
            if len(results.boxes.data.tolist()) > 1:
                for result in results:
                    for r in result.boxes.data.tolist():
                        x1, y1, x2, y2, score, class_id = r
                        x1, x2, y1, y2, class_id = int(x1), int(x2), int(y1), int(y2), int(class_id)
                        
                        # Check presence of predictions history
                        if t_preds[table] != None:
                            # Reset Counter if Draw
                            if (class_id == 1):
                                t_counter[table] = int(0)
                                temp_coords[class_id] = r
                                # try:
                                temp_coords[5] = None
                                # except:
                                    # pass
                            else:
                                try:
                                    # Compare previous coordinates to current coordinates
                                    if (class_id == 0) | (class_id == 2):
                                        for x in coords[table]:
                                            coords1 = np.array(coords[table][x][:4])
                                            coords2 = np.array(r[:4])
                                            are_same = np.all(np.abs(coords1 - coords2) <= tolerance)
                                            if are_same == False:
                                                if table > 3:
                                                    print(f'Table: {table+1}')
                                                else:
                                                    print(f'Table: {table}')
                                                print(coords1)
                                                print(coords2)
                                                print(np.abs(coords1 - coords2))
                                                print(f'before = {t_preds[table]}')
                                                print(f'now = {class_id}')
                                                # print(are_same)
                                            if are_same == True:
                                                break
                                    # Compare prediction with outcome and assign new values.
                                    if are_same == False:
                                        # print(class_id)
                                        # print(t_preds[table])
                                        # print('\n')
                                        if (class_id == 0) | (class_id == 1) | (class_id == 2):
                                            # print(f'before = {t_preds[table]}')
                                            # print(f'now = {class_id}')
                                            if int(class_id) == int(t_preds[table]):
                                                t_counter[table] += 1
                                                if table > 3:
                                                    print(f'+ Table: {table+1}')
                                                else:
                                                    print(f'+ Table: {table}')
                                                # if t_counter[table] > 6:
                                                #     winsound.Beep(440, 1000)
                                            elif int(class_id) != int(t_preds[table]):
                                                t_counter[table] -= 1
                                                if table > 3:
                                                    print(f'- Table: {table+1}')
                                                else:
                                                    print(f'- Table: {table}')
                                                # if t_counter[table] < -6:
                                                #     winsound.Beep(440, 1000)
                                            temp_coords[class_id] = r
                                            # try:
                                            temp_coords[5] = None
                                            # except:
                                                # pass
                                        if (class_id == 3):
                                            temp_preds[table] = 0
                                        if (class_id == 4):
                                            temp_preds[table] = 2
                                except:
                                    # If no previous history, assign values only
                                    if (class_id == 0) | (class_id == 2):
                                        temp_coords[class_id] = r
                                        # try:
                                        temp_coords[5] = None
                                        # except:
                                            # pass
                                    if (class_id == 3):
                                        temp_preds[table] = 0
                                    if (class_id == 4):
                                        temp_preds[table] = 2
                        else:
                            # If prediction history is empty, assign new predictions
                            if (class_id == 3):
                                temp_preds[table] = 0
                            if (class_id == 4):
                                temp_preds[table] = 2
            # Error handling for 1 prediction presence
            elif len(results.boxes.data.tolist()) == 1:
                for result in results:
                    for r in result.boxes.data.tolist():
                        x1, y1, x2, y2, score, class_id = r
                        x1, x2, y1, y2, class_id = int(x1), int(x2), int(y1), int(y2), int(class_id)

                        if (class_id == 0) | (class_id == 2):
                            temp_coords[class_id] = r
                            temp_preds[table] = 5
                        if (class_id == 3):
                            temp_preds[table] = 0
                            temp_coords[5] = 5
                        if (class_id == 4):
                            temp_preds[table] = 2
                            temp_coords[5] = 5
            coords[table] = temp_coords
            try:
                t_preds[table] = temp_preds[table]            
            except:
                pass
            if len(results.boxes.data.tolist()) == 0:
                t_preds[table] = None
                coords[table] = None
                t_counter[table] = 0

        # print(f'final: {coords}')
    return coords, t_preds, t_counter