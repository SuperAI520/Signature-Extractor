# "Signature Extraction" based connected component analysis

A design and implementation of a super lightweight algorithm for "overlapped handwritten signature extraction from scanned documents" using OpenCV and scikit-image on python. ***Please contact if you need professional signature detection & recognition & segmentation & counting project with the super high accuracy!***

---

- Input = The scanned document
- Output = The signatures exist on the input

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47317435-38003480-d652-11e8-87be-0d93ea9e119a.png" | width=750>
</p>

**TODOs:**

- "Outliar Removal" module will be improved to boost the signature extraction algorithm.
- CNN based "Signature Recognition" module will be developed.
- "Signature Spoofing Detection" algorithm will be developed.
- "Signature Detector (bounding box) & Counter" module will be developed.
- "Accuracy of detection on [SigSA: On-line Handwritten Signature Database](http://research.sabanciuniv.edu/13568/1/SigDB.pdf)" will be calculated and shared.

---

#### - Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291471-73781000-d60c-11e8-9e5c-34699d91c73e.gif" | width=450>
</p>

**Explanation:** For this case, the signature extraction algorithm can extract the 3 different handwritten signatures successfully. Just a very small portion of the signature, which is located at top-left, is lost because this part is not connected with the whole signature line so the algorithm interprets it is not a part of the signature.

#### - Sample result#2:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291680-36604d80-d60d-11e8-9a27-6870c6724b0e.gif" | width=450>
</p>

**Explanation:** For this case, signature extraction algorithm can extract 2 handwriteetn signatures from the whole textual data but it can not remove the lines, that are located at bottom-center, because the signature has big connected pixels so the algorithm sees them as signatures.

#### - Sample result#3:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47298403-5b11f080-d620-11e8-9590-a393aeecfe3f.gif" | width=450>
</p>

**Explanation:** Some parts of the signatures are lost because they are not connected with the big connected components so the algorithm sees that they are not a part of signatures. They can cathc by setting the threshold value to a bigger value.

## Installation

**1.) Python and pip**

Python is automatically installed on Ubuntu. Take a moment to confirm (by issuing a python -V command) that one of the following Python versions is already installed on your system:

- Python 3.3+

The pip or pip3 package manager is usually installed on Ubuntu. Take a moment to confirm (by issuing a *pip -V* or *pip3 -V* command) that pip or pip3 is installed. We strongly recommend version 8.1 or higher of pip or pip3. If Version 8.1 or later is not installed, issue the following command, which will either install or upgrade to the latest pip version:

    $ sudo apt-get install python3-pip python3-dev # for Python 3.n
    
**2.) scikit-image**

On all other systems, install it via shell/command prompt:

    pip install scikit-image

If you are running Anaconda or miniconda, use:

    conda install -c conda-forge scikit-image

See details in [here](http://scikit-image.org/docs/dev/install.html).

---
- After completing these 2 installation steps that are given at above, you can test the project by this command:

      python3 signature_extractor.py
---

