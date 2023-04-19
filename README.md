# urinary-stone-segmentation

![image](https://user-images.githubusercontent.com/86519397/233155197-1eb76503-f557-46c0-8348-8cc8e823aca1.png)

Background: - Urinary stones is a serious medical issue that affects 12% of the global population. Ureteroscopy is one such standard diagnostic procedure for urinary stones. Targeting stones during ureteroscopy is challenging due to poor image quality, floating debris, and severe occlusions in the endoscopy video. Automated segmentation and localization of the stone fragments is one potential approach and can improvise the diagnostic accuracy while conserving time. Deep learning networks have proven to perform well in automated segmentation tasks.
Objective: - To develop an algorithm for automated segmentation of urinary stones using deep neural networks. 
Materials and  Methods: 1020 ureteroscopy frames containing urinary stones were collected retrospectively for this work. The ground truth annotations for the urinary stones were manually marked by experts. The proposed architecture for automated segmentation is a EfficientNetB2 based U-Net. The training dataset comprises of 80% of data and the remaining 20% was allotted to validation. The trained algorithm was deployed into a user interface for real time diagnostic usage. The proposed user interface segments the region of urinary stone and also identifies the composition material of the stone along with its severity. 
Results: - The proposed architecture produced 90% dice score, 93% jaccard score, 96% precision and 87% recall on testing data. 
Conclusion: - Hence a deep learning algorithm and a real time user interface has been developed. Urologists may be able to employ the proposed algorithm in real time for dynamic and effective segmentation of urinary stones to support their surgical and medical decision-making skills.

website link:- 
