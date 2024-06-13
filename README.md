# Vehicle Detection Project using YOLOv8 and KITTI Dataset

## Introduction
This project aims to detect vehicles using a dashboard camera mounted on a vehicle, leveraging the YOLOv8 model and the KITTI dataset. The project not only focuses on vehicle detection but also lays the groundwork for future enhancements such as detecting different types of vehicles and estimating their speed.
![val_batch2_pred](https://github.com/jaliyanimanthako/kitti-object-detection/assets/161110418/cf44aa52-4e46-4894-a509-b81d7031ab49)


## Dataset
### KITTI Dataset
The KITTI dataset is one of the most popular datasets for various computer vision tasks, particularly for autonomous driving. It offers a variety of challenging real-world computer vision benchmarks. The tasks of interest include stereo, optical flow, visual odometry, 3D object detection, and 3D tracking.

To create this dataset, the KITTI team utilized their autonomous driving platform, Annieway. They equipped a standard station wagon with two high-resolution color and grayscale video cameras. Accurate ground truth data is provided by a Velodyne laser scanner and a GPS localization system. The dataset captures scenes from the mid-size city of Karlsruhe, rural areas, and highways. Up to 15 cars and 30 pedestrians are visible per image.

Besides providing all data in raw format, KITTI extracts benchmarks for each task and provides evaluation metrics and an evaluation website. The dataset's goal is to reduce the bias seen in laboratory conditions and offer real-world benchmarks with novel difficulties to the community.

<p align="center">
<img src = https://github.com/jaliyanimanthako/kitti-object-detection/assets/161110418/bb71f764-696e-4ba0-bc1a-1a61634a12d0>
</p>

Current object classifications in the KITTI dataset include:

The KITTI dataset currently classifies objects into the following categories:
- Car
- Pedestrian
- Van: 2
- Cyclist
- Truck
- Misc
- Tram
- Person_sitting
- DontCare

For more details, visit the [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/).


## Model
### YOLOv8 by Ultralytics

<p align="center">
<img src = https://github.com/jaliyanimanthako/kitti-object-detection/assets/161110418/462e3dcd-042d-47d9-ba9f-24cb6278e476>
</p>

YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system. YOLOv8, the latest iteration by Ultralytics, introduces several improvements over its predecessors:
- Improved accuracy and speed.
- Better architecture and data augmentation techniques.
- Enhanced training process.

<p align="center">
<img src = https://github.com/jaliyanimanthako/kitti-object-detection/assets/161110418/10485688-9945-4557-8a97-9ba7b594035d>
</p>
The performance of our YOLOv8 model on the KITTI dataset is visualized using a normalized confusion matrix. This matrix provides insight into the model's accuracy and the misclassification rates across different categories.

From the confusion matrix, we can observe:

- High Accuracy for Car Detection: The model correctly identifies cars with an accuracy of 92%.
- Misclassification of Pedestrians and Cyclists: There are notable misclassifications between pedestrians and cyclists, with a significant percentage of cyclists being misclassified as pedestrians.
- Van and Truck Detection: Vans and trucks also show high accuracy, but there is room for improvement to reduce the confusion between these categories.
- Background Detection: The background category shows a high level of misclassification, indicating that further refinement is needed to improve the model's ability to distinguish between objects and the background.
For more details, visit [Ultralytics YOLO](https://github.com/ultralytics/ultralytics).


## Further Developments
### Future Enhancements

1. **Vehicle Direction Detection**:
    - Extend the model to detect the direction in which vehicles are moving.
    - Use additional datasets or augment the KITTI dataset with more labeled data to improve direction detection.
      
2. **Speed Detection**:
    - Integrate optical flow techniques or employ multi-frame analysis to estimate the speed of detected vehicles.
    - Leverage sensor data from the dashboard camera if available.

### Research and Improvements
- Experiment with different versions of YOLO and other object detection models.
- Fine-tune hyperparameters and augment the dataset for better accuracy and robustness.
- Implement real-time processing capabilities and optimize for deployment on edge devices.

## Sri Lankan Road Traffic Accidents
### Overview

![image](https://github.com/jaliyanimanthako/kitti-object-detection/assets/161110418/aefc2d9f-1b82-4723-964f-1c3f791de056)

Sri Lanka has a significant issue with road traffic accidents, largely attributed to careless driving. According to recent statistics:
- **Annual Traffic Accidents**: Over 35,000 traffic accidents occur each year.
- **Fatalities**: Approximately 3,000 fatalities annually.
- **Common Causes**: Speeding, reckless driving, and non-adherence to traffic rules.

### Potential Solution
This vehicle detection project can be expanded to address this issue by:
1. **Real-Time Traffic Monitoring**:
    - Deploy the vehicle detection system on traffic cameras across Sri Lanka.
    - Monitor for reckless driving behaviors and alert authorities in real-time.

2. **Speed Detection and Penalty System**:
    - Integrate speed detection to identify speeding vehicles.
    - Automatically issue penalties or warnings to violators.

3. **Driver Assistance Systems**:
    - Develop an advanced driver-assistance system (ADAS) for vehicles.
    - Provide real-time alerts to drivers about potential hazards, including other reckless drivers.

4. **Data Analytics for Traffic Management**:
    - Use the collected data to analyze traffic patterns and identify accident-prone areas.
    - Implement measures to improve road safety in these areas.

By leveraging this technology, Sri Lanka can significantly reduce traffic accidents and enhance road safety for all users.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements, bug fixes, or new features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- The KITTI Vision Benchmark Suite for providing the dataset.
- Ultralytics for developing and maintaining YOLO.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!
