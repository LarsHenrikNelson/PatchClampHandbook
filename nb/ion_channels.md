# Ion channels
This chapter will cover some of the major ion channels and how they effect neural function. Each section is not a comprehensive coverage of the channels but act more as a starting point. I will not cover structure of the channels unless is pertains to how it relateds to the function of the cell. We cover ion channels because they are the primary way which charge or current can go across the membrane. The membrane is practically impermeable to ions thus the neurons need a way for charge to distribute itself across the membrane. Ion channels are also resonsible for setting the resistance of a neuron. Simplistically, the number of opened and closed channels sets the membrane resistance. The distribution of types of ion channels and their functional properites in turn sets the functional properties of the neuron.
Ion channels can come in three different types; voltage-gated, ligand-gated and persistantly open channels. Voltage-gated channels open and close dependent on voltage. Ligand-gated channels need need a ligand to bind to open the channel. Factors such as cAMP or allosteric modulators, can change ion channel function. The ion channels expressed by a cell determine features such as spike shape, ability to burst, adaptation of spikes over long trains of spikes, pacemaking activity, and synaptic release [@beanActionPotentialMammalian2007]. One general feature of ion channels is they can have an outward or inward preference for current passage which is called rectification. Many ion channels will not conduct currents in both directions with equal magnitude. For example, this means we have different channels that are primarily responsible K+ going into the cell and out of the cell [@nisenbaumPotassiumCurrentsResponsible1995]. It is important to understand that ion channel regulates neuronal function through expression levels **AND** location of ion channel in a cell. HCN channels are probably one the most ubiquitously expressed ion channels but has very different function depending on the cell type due to location of the channel. Throughout this chapter I will use the [Allen Institute's Allen Brain Cell (ABC) Atlas](https://brain-map.org/bkp/explore/abc-atlas) to show how gene expression differs between a select number of neuronal subtypes in the mouse brain. Each channel type section will have a plot showing a heatmap of expression. I selected a set of notable cell types; pyramidal (hippocampus and cortical), cortical interneurons (SST, PV, and VIP), striatal neuron (MSN), spontaneously spiking neurons (Cholinergic (STR) and VTA Dopa), VTA interneuron (some spontaneously spike) and cerebellar neurons (Purkinje, Granule and molecular layer interneuron).

## Sodium channels
### Voltage-gated sodium channels
Voltage-gated sodium channels are generally needed for a cell to generate an action potential. Voltage-gated sodium channels consist of an alpha and beta subunit. The alpha subunit is the ion conduction portion of the channel. The beta subunit helps anchor the alpha subunit to the membrane and can also change the kinetics of the alpha subunit. There are several isoforms of the alpha subunit of these channels that have different activation, deactivation and deinactivation kinetics, and sensitivity to pH. Most Voltage-gated sodium channels are also sensitive to TTX except for Scn5a (Nav1.5), Scn10a (Nav1.8), and Scn11a (Nav1.9). We use TTX in slice electrophysiology to stop activity dependent synaptic release or to determine how much current/resistance voltage-gated sodium channels are contributing to a cell at a specific voltage (usually just at rest). In the central nervous system, Scn1a (Nav1.1), Scn2a (Nav1.2), and Scn8a (Nav1.6) are the primary voltage-gated sodium channels with some cells expressing Scn3a (Nav1.3) and Scn9a (Nav1.7) [@wangDistributionFunctionVoltagegated2017]. The main difference between ion channels is their primary location within the neuron. Scn1a is primarily located cell body and Scn8a is primarily located in the nodes of Ranvier during adulthood. Scn2a is the primary voltage-gated sodium channel in the nodes of Ranvier during development and is also expressed in the axon initial segment. Another difference in voltage-gated sodium channels is cell type differences in expression. Notably, PV interneurons express a large amount of Scn1a compared to other neurons which is probably related to their ability to fire at high rates. Scn9a (Nav1.7), Scn10a (Nav1.8), and Scn11a (Nav1.9) are primarily expressed in the peripheral nervous system. Scn10a is a unique voltage-gated sodium channel that is highly invovled in peripheral pain (#https://en.wikipedia.org/wiki/Nav1.8).
```{image} ../data/gene_figures/na.png
:alt: Voltage-gated sodium channel gene expression
:align: center
```

### NALCN
NALCN is a persistantly open sodium channel.

## Potassium channels
Potassium channels are the most diverse set of ion channels in the brain. The regulate the resting membrane potential, action potential threshold, and the afterhyperpolarization depending on the cell type.

### Inwardly rectifying (Kir)
Inwardly rectifying potassium channels, also called Kir channels, conduct current *into* a cell when the cell is at more hyperpolarized voltages and conduct very little outward current. Kir channels are endogenously blocked at depolarized potentials by Mg++ and spermine [@hibinoInwardlyRectifyingPotassium2010]. As the cell membrane becames more negative Mg++ and spermine are pulled into the pore, similar to how Mg++ is pushed away from the outside of the membrane from NMDA receptors (this is related to a concept called surface charge). Interestingly as these channels get block it will also increase the membrane resistance. Celltypes, like MSNs in the striatum, that have a very hyperpolarized resting  potential of around -80 ot -90 mV express very high levels of Kir. The Kir channels are Kcnj1, Kcnj2, Kcnj4, Kcnj8, Kcnj10, Kcnj11, Kcnj12, Kcnj13, Kcnj14, Kcnj15, and Kcnj16.
```{image} ../data/gene_figures/kir.png
:alt: Kir channel gene expression
:align: center
```

### GIRK channels
GIRK channels are G protein-coupled inwardly rectifying potassium channels. GIRK channels are opened when the &#946;&#947; G protien subunits interacts with the GIRK channel. GIRK channels are thought to be one of the primary ways that DREADDs change the excitability of the cell. The GIRK channels are Kcnj3, Kcnj6, Kcnj9 and Kcnj5.
```{image} ../data/gene_figures/girk.png
:alt: GIRK channel gene expression
:align: center
```

### SK channels
SK channels as small conductance calcium-activated potassium channels. They are activated by an increase calcium primarily through N-type calcium channels. SK channels can limit excitatory postsynaptic potentials, regulate Ca++ signaling, limit intrinsic excitability and affect pacemaking activity [@foisStructureFunctionPharmacology2026]. The SK channels expressed in the brain are Kcnn1 (SK1), Kcnn2 (SK2), and Kcnn3 (SK3). Kcnn4 is not expressed in the brain. The primary blocker of SK channels is apamin, a peptide toxin [@foisStructureFunctionPharmacology2026]. Apamin blocks SK1 and SK3 with lower potency. There are a host of other synthetic SK channel blockers with varying potency and selectivity [@foisStructureFunctionPharmacology2026].
```{image} ../data/gene_figures/sk_channel.png
:alt: SK channel gene expression
:align: center
```
### BK channels
BK channels are large conductance Ca++-activated and voltage-activated potassium channels. They contribute to the repolarization of the action potential, the fast after-hyperpolarization potential, synaptic release and membrane excitability [@sahChannelsUnderlyingNeuronal2002, @contetBKChannelsCentral2016]. BK channels a composed of a single pore-forming alpha subunit, Kcnma1. There are also $\beta$ and $\gamma$ subunits that determine the Ca++- and voltage-sensing properties, kinetics and function of the $\alpha$ subunit [@liModulationBKChannel2016]. The $\beta$ subunit are Kcnmb1, Kcnmb2, Kcnmb3, and Kcnmb4. The Kcnmb4 and Kcnmb2 are the primary subunits expressed in the CNS. Kcnmb1 and Kcnmb2 slow kinetics and increase Ca++ and voltage sensitivity [@liModulationBKChannel2016]. Kcnmb4 reduces Ca++ sensitivity in a dose depedent manner [@liModulationBKChannel2016]. The $\gamma$ subunits are Lrrc26 ($\gamma 1$), Lrrc52 ($\gamma 2$), Lrrc55 ($\gamma 3$) and Lrrc38 ($\gamma 4$). The $\gamma$ subunits seem to largely drive activation towards hyperpolarizing voltages [@liModulationBKChannel2016].
```{image} ../data/gene_figures/bk_channels.png
:alt: BK channel and subunit gene expression
:align: center
```

### Low-threshold potassium channels (M current/Kv7)
Low-threshold potassium channels channels produce an outward current, are open at near resting membrane potential and lack inactivation (open or closed)  [@greeneModulationKv7Channels2017]. The Kv7 channels are very important for setting the membrane potential at the axon intial segment. Currents throught these channels have been termed M-current since they were discovered when the muscarinic acetylcholine receptor (MAchR 1 and 3) channel is activated altered the potassium current. There are a variety of Gq coupled receptors that supress the channel. The low-threshold potassium channels are Kcnq1 (Kv7.1), Kcnq2 (Kv7.2), Kcnq3 (Kv7.3), Kcnq4 (Kv7.4), and Kcnq5 (Kv7.5). Kcnq1 is not expressed much in the CNS. You can blocker Kv7 channels with XE991.
```{image} ../data/gene_figures/low_current_k.png
:alt: Low-threshold potassium channel gene expression
:align: center
```

## Calcium channels
### Voltage-gated calcium channels
Voltage-gated calcium channels are generally grouped into high and low voltage-activated types (HVA and LVA respectively) [@simmsNeuronalVoltageGatedCalcium2014]. High voltage-activated channels need large membrane depolarizations to open and low voltage-activated channels only need to small membrane depolarizations to open and can open near the resting membrane potential. Calcium channels can be further subdivided into several subtypes; T-type, P/Q-type, N-type, L-type (Cav1) and R-type. All calcium channels have a Cav&#945;1 subunit and only high-voltage channels have ancillary subunits Cav&#945;2&#948; and Cav&#946;. Cav&#946; regulates the voltage-dependent inactivation HVA channels. All calcium channels show voltage-dependent inactivation and some channels also show calcium-dependent inactivation. The P/Q-type channels show calcium-dependent facilitation. Voltage-gated calcium channels typically open during the falling phase of the action potential [@beanActionPotentialMammalian2007], and involved in synaptic transmission (particularly P/Q-, and N-type).

#### L-type (Cav1)
L-type channels have slow voltage-depedent gating properties (long-lasting currents) and are part of the HVA family. L-type channels are important for activation of CREB and regulation o gene expression. L-type channhels are sensitive to 1,4-dihidropyridine (DHP). L-type calcium channels are Cacna1s (Cav1.1), Cacna1c (Cav1.2), Cacna1d (Cav1.3), Cacna1f (Cav1.4). 
```{image} ../data/gene_figures/ltype_ca.png
:alt: L-type calcium channel gene expression
:align: center
```

#### P/Q-type (Cav2.1)
P/Q-type channels are involved in fast synaptic transmission and expressed in the presynapse to facilitate vesicle release.The P and Q-type channels are encoded by the Cacna1a (Cav2.1) gene that is alternatively spliced to produce each of the subtypes [@simmsNeuronalVoltageGatedCalcium2014]. P/Q-type channels are also regulated through several G protein coupled pathways [@catterallVoltageGatedCalciumChannels2011].
```{image} ../data/gene_figures/pqtype_ca.png
:alt: P/Q-type calcium channel gene expression
:align: center
```

#### N-type (Cav2.2)
N-type channels are involved in fast synaptic transmission and expressed in the presynapse to facilitate vesicle release. The N-type calcium channels are encoded by the Cacna1b gene. N-type channels are also regulated through several G protein coupled pathways [@catterallVoltageGatedCalciumChannels2011]. N-type chanels are well known to activate SK channels.
```{image} ../data/gene_figures/ntype_ca.png
:alt: N-type calcium channel gene expression
:align: center
```

#### R-type (Cav2.3)
N-type channels are involved in fast synaptic transmission and expressed in the presynapse to facilitate vesicle release. The N-type calcium channels is encoded by the Cacna1e gene.
```{image} ../data/gene_figures/rtype_ca.png
:alt: R-type calcium channel gene expression
:align: center
```

#### T-type (Cav3)
T-type channels are part of the LVA family so they do not contain any ancillary subunits. T-type channels are involved in presynaptic vescicular release. They are expressed in the postsynapse and help drive dendritic axon potentials. They also help facilitate the activation of voltage-gated Na+ channels. T-type channels have also been implicated in pacemaking activity [@beanActionPotentialMammalian2007; @catterallVoltageGatedCalciumChannels2011; @simmsNeuronalVoltageGatedCalcium2014]. T-type calcium channels are also regulated by G protein signaling [@catterallVoltageGatedCalciumChannels2011]. T-type channels are Cacna1g (Cav3.1), Cacna1h (Cav3.2) and Cacna1i(Cav3.3).
```{image} ../data/gene_figures/ttype_ca.png
:alt: T-type calcium channel gene expression
:align: center
```

## Other channels
### HCN channels
Hyperpolarized-activated cyclic nucleotide channels are cation channels that open when a cell becomes hyperpolarized below ~-40 mV and whose kinetics can be altered by cyclic nucleatide (in particular cAMP). There are four variants each with different kinetics and sensitivity to cAMP. HCN channels primarily conduction Na+ and K+. These subunits have differences in activation speed where activation speed fast to slowest 1 &rarr; 2 &rarr; 3 &rarr; 4 [@sartianiHyperpolarizationActivatedCyclicNucleotide2017]. cAMP can also allow HCN channels to open faster and at more depolarized levels where sensitivity is most to least 4 &rarr; 2 &rarr; 1 &rarr; 3. Lastly HCN channel opening is faster at more negative voltages with voltage sensitivity being different among the channels.
One important thing about HCN channels is that many cell types express HCN channels but the location of the protein is cell-dependent and related to how HCN currents are involved in neuronal function. HCN channels are highly expressed in pacemaking neurons like midbrain dopaminergic cells. While HCN channels contribute to pacemaking activity they are not essential to pacemaking activity [@neuhoffIhChannelsContribute2002; @chanHCN2HCN1Channels2004]. They are more modulators of pacemaking activity governing pacemaking speed and regularity. When HCN channels are expressed on the presynapse, such as in PV interneurons, they can change the synaptic release probability by regulating Ca++ levels through T-type Ca++ channels (remember HCN channels are permeable to Na+) [@bussHCN1HyperpolarizationactivatedCyclic2024; @caiPresynapticHCNChannels2022]. HCN channels expressed in axons of PV basket cells helps sustain high frequency firing [@rothAxonspecificExpressionHCN2020]. When HCN channels are expressed in the spines and dendrites they may help set the level of excitatory input needed to drive an action potential. HCN channels also contribute to resonance since they make membrane resistance nonlinear.
```{image} ../data/gene_figures/hcn.png
:alt: HCN channel gene expression
:align: center
```