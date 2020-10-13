If you are on linux you can run the executable
Otherwise install pyqt5 and run the python file

Enter the number of samples and the prevalence to calculate the pool size and number of pools for the first round
press enter or press the button to calculate

The pool size is automatically added to the second round, the user has the ability to change it in case they want
a different set up, press enter or press the button to calculate

The assumption is that the samples are labelled using digits 1, 2, 3 ... up to the last sample

After running for the second round, samples in each slice are displayed in the output tab; the user chooses a direction on the tab (D1, D2, ... ), 

and a color in the dropdown; only three colors are used (Yellow, Red and green)

After testing the samples, positive slices are added by choosing their direction and color then press OK to find out which samples are positive.

In case the process in not deterministic, the software automatically stages a retest and calculate slices for each of the positive direction.

Again after testing positive slices are entered in the software to find out which samples are positive.

NB: For now only one subtest is assumed.
    
The sofware can save and open .hcb files (hypercube files). 

The compiled executable doesn't save and open, problem being fixed ASAP.


