# Recording from cells
## Placement of slice on the rig
How you place your slice on the rig will generally be dependent on where your are recording from. Generally, if possible, try to align the midline to either the top/bottom or left/right, rather than going an angle. This gives you a point of reference and an easy way to measure how far from top/bottom or side/midline. Next you will want to place a harp on your tissue to prevent it from sliding around. Harps can be a simple wire, either straightr or curved, or they can be a curved wire with a thin string glued across to help weigh down the tissue. I recommend using gold wire if possible. It is expensive but is the most dense affordable metal you can use. Steel and aluminum wires tend to be too light. If you use steel make sure to get corrosion resistant steel since regular steel with corrode quickly with all the salts in the bath.

## Finding cells
Finding good cells can be challenging when you first start. You should generally avoid cells on the top of the section. I typically look for cells about 30-60 uM below the surface of the tissue. Cells should not have dark borders, look shrunken, look swollen or have a clearly visible nucleus. The shape of the cells will depend on the area you patch in. Pyramidal cells in the cortex look like rounded triangles, interneurons are generally round, MSNs are also round, cholinergic interneurons in the striatum are massive. When you start it can be help to use tape to mark where your cell is on the computer screen (if you have that). You can also zero the microscope z-axis at the top of the tissue to measure how deep your section is if you are using an electronically control z-axis.

## Preparing the electrode for patching
- First you want to pull your pipette. 
- Then fill it with your internal. The best way to fill a pipette is to use a microfil and make sure to use a 22 uM filter between the syringe and microfil/needle. The filter prevents large chunks of salts or other stuff from getting into your pipette which will clog your pipette. 
- Next you want to carefully flick the pipette to get the bubbles to rise from the sharp tip. Bubbles in the tip will ruin a recording and can prevent you from getting a good seal on a cell. 
- Attach your glass pipette to the electrode holder
- Put some positive pressure into the pipette. I generally recommend doing this before you move the pipette into the recording well. Once you place your pipette into the liquid any debris will be attracted stick to the pipette and ruin your pipette. The positive pressure ensures that all that debris is blown away. If you are using a manometer to track the presssure of your pipette I recommend no more than 30 mBar.
- Lower your pipette into the bath.
- Make sure you are in voltage clamp mode. Also make sure you are not clamping the voltage.
- Turn on your test pulse. The test pulse will tell you the resistance of the pipette. It can be a positive or negative pulse, 5-10 mV about 10-20 ms long.
- You will want to remove the pipette offset. This is the voltage difference between the pipette and ground. This does not correct for the junction potential but, it is essential to remove the offset since this means you have a non-zero current between your pipette and ground. The larger this current is the more inaccurate your recordings will be. Note that on some equipment you may see voltage such as 20.2 mV and other equipment may read 0 afterwards. The equipment that reads a non-zero voltage is just telling you how much voltage difference is being offset.

## Getting a cell
- To get down to the tissue, lead with the microscope and follow with the pipette. Leading with the microscope prevents you from crashing the pipette into the tissue which will ruin the cells in the surrounding area.
- As you get close to the tissue you will want to position your pipette towards the edge of the screen if your cell is centered in the screen. As you lower your pipette into the tissue you should see the tissue blow away from your pipette.
- You will want to move to the cell on the z-axis and move in the x/y-axis simulateneously. Alternatively you can use the angle function on the probe holder. As you go towards the cell avoid other cells, axons and other debris
- As you get close to the cell I recommend lowering the pressure to ~10 mBar so you don't blow the cell away. As you lower the pressure you may notice the tissue flows back towards the pipette.
- Remove the pipette offset before you attempt to patch onto the cell.
- You should try to sit on top of the cell rather than go under the cell.
- When you get to the point where you could form a GOhm seal you should see a dimple in the cell or see the pipette resistance increase by 0.1-0.2 MOhm.
- Release the positive pressure. Usually the membrane kind of springs into the pipette tip. You can also apply some light negative pressure.
- If you got a seal you should see the resistance start to increase to at least 100-200 MOhm. At this point you can set the holding voltage to -70 mV or where ever you prefer. Most cells will form a better GOhm seal if you turn on a -70 mV holding potential but, it is not technically necessary.
- Once you get a GOhm seel you can break into the cell. You can do this by creating a sudden, brief negative pressure. If you want to you can simultaneously hit the zap button if your amplifier has it. I use a 50 us zap. The zap outputs a strong current from your electrode that can help dissolve the membrane and reduce your access resistance.
- Once you break in you need to immediately record the membrane resistance and the capacitance since these usually change as the internal perfuses the cell. Additionally, you can check the resting membrane potential by switching to I=0 mode or current clamp mode with no current clamped.
- Just wait a couple minutes for the internal to perfuse throughout the cell.
- Before you record make sure that the series/access resistance (Rs or Ra) is below 20-25. You can also use the whole cell or series/access resistance compensation.