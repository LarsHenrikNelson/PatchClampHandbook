# Troubleshooting your experiments
There are several common issues you can have in your experiments that we will cover here.

## Cells are swelling after breaking in
The most common cause of cell swelling after breaking in is an osmolarity mismatch between the internal and external solution. If it is a one off occurance you can increase the osmolarity of the external solution by adding glucose or sucrose. If this issue is persistant you need adjust either your internal or external recipe. It is usually easiest to adjust the external solution by adding more glucose.

## Cells are shrinking after breaking in
The most common cause of cell shrinking after breaking in is an osmolarity mismatch between the internal and external solution. If it is a one off occurance you can lower the osmolarity of the external solution by adding water. If this issue is persistant you need adjust either your internal or external recipe. It is usually easiest to adjust the external solution by removing more glucose.

## My cells are dying shortly after breaking in
If you have this issue persistently, there are two common causes. The osmolarity difference between your internal and external solution is too big or if the internal lacks enough ATP, GTP or phosphocreatine due to the recipe (probably uncommon) or the reagents have degraded (stored at too warm of temperatures). The most common cause is that something just went wrong making the external or preparing the tissue.

## Cannot see any cells
There are probably several reasons for this. This is usually a one off occurance. I know from personal experience if you forget the KCl in the external solution you will not see any cells nor is the tissue recoverable. If you are having consistent issues check your pH and osmolarity. Also if you use stocks of ions like KCl, MgCl2 or CaCl2. Since you only add a little bit of these your external solution it is really hard to tell if you accidentally left them out or if your stock is off.

## There is a lot of 60 Hz in my signal
If you see a large amplitude sinusoidal signal in your data, you most likely have 60 Hz contaminating your signal chain. You always need to ground some of the equipment to the floating table you record on. You can also connect a wire from the table to a copper pipe (most common, not optimal) in the wall or a dedicated ground connect in the room (pretty rare). Another reason for 60 Hz is that your bath is to low or your ground is partly out of the bath. The ground should be covered enough that you have a perfect sphere or pool of water over your slice. If you see a lump where the ground is increase the bath level.

## I cannot see any signal
If you cannot see the test pulse when the pipette is in the bath this usually means you have a break in the circuit somewhere on the rig. The most common reason for a break in the circuit is a broken ground wire connecting to your ground pellet. Another potential cause is the electrode wire is not correctly contacting the metal pin in the electrode holder. Check that your signal chain between your ADAC and ampfilier are correctly setup. Lastly, make sure your software is configured correctly.