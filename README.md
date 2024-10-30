# A web application for predicting weld sizes in electron beam welding of thin-walled aerospace structures.

The initial data were the results of experimental
studies conducted in order to improve the technological process
of electron beam welding of a product, the assembly of which consists of elements
consisting of heterogeneous material.
The electron beam welding unit, where the research was carried out, is designed for welding with an electron beam in high vacuum
parts of assembly units made of stainless steels, titanium, aluminum
and special alloys.

**The model is trained according to the following criteria**: 
  * Welding current value (IW);
  * Electron beam Focusing current (IF);
  * Welding Speed (VW);
  * The distance from the surface of the samples to the electron-optical system (FP).
    
According to the set of parameters of technological modes, the minimum possible sizes of welds were provided: the depth of the seam (Depth) and the width of the seam (Width)

The launch is performed as a standard flask application: ```python app.py```
