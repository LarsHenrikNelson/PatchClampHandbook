# Patch clamp electrohysiology equipment
There are several pieces of core equipment that you will need to run a patch clamp rig. You will also need to understand the signal flow to be able set up a new rig or troubleshoot an old rig. You do not need the newest equipment to patch well or get good data. Companies that sell electrophysiology equipment include (in alphabetical order) A-M Systems, Automate Scientific, Digitimer, CoolLED, Luigs and Neumann, Molecular Devices, Nation Instruments, Scientifica, Sensapex, Siskiyou, Sutter, Thor Labs, and TMC among others.

## The rig
### Microscope
You will need a microscope. Microscopes can be either fixed to a platform or on a low friction movable stage. If the microscope it fixed to a platform then your manipulators will generally be on a movable stage along with the the slice well. Microscopes come from a variety of companies.
::::{grid} 2
:::{grid-item}
```{figure} ../data/ephys_rig/microscope.JPEG
:height: 250px

Olympus BX51WI with manual micrometers
```
:::
:::{grid-item}
```{figure} ../data/ephys_rig/luig-neumann-rig.JPEG
:height: 250px

Luigs-Neumman microscope with motors
```
:::
::::

### Optics
You will need a microscope with [differential inference contrast](https://en.wikipedia.org/wiki/Differential_interference_contrast_microscopy), [Dodt gradient contrast](https://www.scientifica.uk.com/learning-zone/dodt-gradient-contrast), or a polarized bright light system (very old school but it works). If you want to do channelrhodopsin stimulation you will need either a mercury bulb light or more modern LED system. Usually these systems will be paired with a filter cubes in the upper part of the microscope. CoolLED seems to have a monopoly on the LED systems that labs use and mercury lamps are much less common.

### Camera
While cameras are not essential they are pretty much standard on most rigs, even older ones. A lot of companies sell cameras and a lot of the time they come included with the rig. Older cameras tend to be CCD but newer cameras seem to moving towards scientific CMOS sensors. If you want to take videos you will definitely want one a camera with the large aluminum body since this helps with cooling. Some cameras come with their own software like Thor labs and for others you can generally run them with [MicroManager](https://micro-manager.org/). There are some electrophysiology programs that have control the cameras directly in the software especially if the offer some sort of automated patch-clamp.
::::{grid} 2
:::{grid-item}
```{figure} ../data/ephys_rig/thor-camera.JPEG
:height: 250px

Thor labs scientific CMOS camera.
```
:::
:::{grid-item}
```{figure} ../data/ephys_rig/electro-camera.JPEG
:height: 250px

Electro CCD camera.
```
:::
::::

### Manipulators
Most manipulators for patch clamp electrophysiology are motorized since they provide a lot more fine control. For using a stimulus probe you can use a manual manipulator. The biggest difference between manipulators is whether the Z-axis is angled or flat. The probe its self is always angled but the the manipulator can move at that angle or a stand flat axis. Luigs and Neumman manipulators default to angled and others like Scientifica defualt to flat.
Motorized manipulators come with two types of controller. Usually there is a large flat one that controls the microscope and a smaller one to control the manipulator. Motorized manipulators will have a fine and coarse control for all axes while manual manipulators may have a fine axis for only one axis.

### Amplifier
You can do electrophysiology experiments without an amplifier. The amplifier controls the currents going into a cell and the voltages the cells are held at. The amplifier allows us to record very tiny signals. The amplifier controls the mode of recording; voltage clamp, I=0, and current clamp. The amplifier has to connect to a headstage. The headstage is where the glass electrode goes. The headstage and amplifier are usually calibrated to work together so they usually come from the same company. Molecular Devices has a good book on how the headstage and amplifier work in a theoretical sense.

### Digitizer
The signals we get from the amplifier are analog and need to be digitized to be saved on the computer. Digitizers, also called DACs for short, turn our computer code into analog signals that the amplifier can "understand". While a lot of companies that make amplifiers also make digitizers, some companies specialize in high performance digitizers like Nation Instruments.

## Signal flow
Now that we covered the essential electrophysiology rig components you need to understand the signal flow in the rig. The diagram below has arrows showing the direction that signal goes. The only bidirectional signals are between the computer and the DAC, and the DAC and the amplifier.
```{image} ../data/ephys_setup.svg
:alt: Electrophysiology rig signal flow
:align: center
```
To make sure the DAC and amplifier are hooked up correctly the output of the DAC must go to the command of the amplifier. The output of the amplifier must go to the input of the DAC. You must also have a ground pellet connected to the headstage. The ground pellet and headstage (usually ACSF) must both be immersed in the same dish of solution to get a signal. The ground pellet is local reference and separate from an equipment ground. The equipment ground is mostly for safety.

## Other equipment
### Pipette puller
You will need some sort of pipette puller. I have only seen the Sutter P1000 pipette puller which relies a heated filament and solenoids to detect velocity of the separating glass. I have heard some labs still use a gravity based puller system but I have not seen one in action.

### pH meter
You will need a pH meter to test the pH of your solutions. There are many brands that will work will. I recommend getting a pH electrode that does not have an internal fill solution since they are easier to maintain.

### Osmometer
Osmometer is also essential to makes sure the solutions you make have the omsolarity/osmolality that you expect. There are two types; vapor pressure and freezing point depression. The freezing point depression osmometers are supposed to be better for biological solutions. Vapor pressure do better with volatile solutions. However, both will work and the vapor pressure osmometers tend to be cheaper to run but seem to me to be more variable.

### Microforge
A microforge is used to fire polish the tip of the pipette. Some pipette pullers clame to do this too so this equipment is not essential. The microforge also allows you to inspect the pipette tip. This can be useful for intracranial glass injection pipettes but is less needed for slice electrophysiology.

### Line noise attenuator
Some times line noise is very large and can ruin your recordings. If you have tried everything to get rid of the line noise then you can use special equipment, like the HumBug, to remove the line noise. Some digitizers, like the Axon 1500B, have line noise removal built in. I would use a line noise attenuator as last resort since.

### Stimulators
If you want to get the paired-pulse ratio or do LTP/LTD experiments the you will need a stimulator. They can be controlled by TTL and allow you to "inject" macrocurrents into your tissue slice. You will need a stimulus electrode that connects to the stimulator. THe electrodes can be handmade or purchased.