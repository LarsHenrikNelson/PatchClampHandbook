(designing_current_clamp_exp)=
# Designing a current clamp experiment
Current clamp recordings are one of the most common patch-clamp experiment. Current clamp experiments allow you to get the active parameters of cells. Namely gain, rheobase and spike threshold. Current clamp recordings typically use stepped currrent injections or ramps and you are investigating the voltage change due to the current injection and whether and how the cell spikes. The current clamp chapter is divide into two parts. The first part is a basic analysis and covers what features we look for and why they are important. The second part will delve much deeper in relationships between spike features and cover differences between a few cell types; pyramidal cells, spiny projection neurons and parvalbumin interneurons. Before starting a very good reference for current clamp experiments and their endpoints is the Allen Institute white paper on electrophysiology. I recommend looking it over.

## Experimental considerations for current clamp recordings
### Internal and external solutions
You will need to a standard ACSF for recording. Many labs mantain the ACSF at physiological temperatures which is considered ~32&deg;C however you can record at room temperature but, reviewers may not like it. I recommend recording at 30-32&deg;C. You can include drugs in the bath to block synaptic activity but do not need to include these. If you are having a lot of recurrent input that is driving spikes, depolarizations or hyperpolarizations in your cells if may be good to include some drugs to block synpatic currents. The one problem with blocking synaptic currents there can be homestatic changes in cell functin due to changes in or lack of synaptic input. These are considerations you need to consider. I would recommend starting without any drugs in the bath to keep it simple.

### To use a holding current or not
One thing to consider is whether you should inject a slow holding current to bring the cell to a specific resting potential value. Some labs inject current to hold the cell at around -70 mV or the cell-type's resting membrane potential and run their current pulses or ramps based on that holding current. There other labs that do not inject any holding current and even argue against injecting any holding current. One thing to consider is how you are measuring membrane resistance. HCN channels and other voltage gated channels opening and closing changes with membrane voltage. So if have two cells have a different $V_{rest}$ then the membrane resistance values you get are could be different simply because they are at different $V_{rest}$ due to differences in the number of voltage-gated that are open or closed, however you will be getting a more realistic measure of the linear portion of membrane resistance. For measurements such as membrane I recommend measuring without injecting a slow current. Another question is whether rheobase is the current it takes to get a cell to spike from a specific membrane voltage or from where the resting membrane potential is? Here is an example to consider. It takes 50 pA to get a layer 5 pyramidal in a WT mouse to fire an action potential from -70 mV and in a knockout mouse it takes 100 pA. However, the WT mouse cells sits a -70 mV at baseline where as knockout mouse sits as -60 mV. What if there is no difference in the rheobase current? What if there is a difference in rheobase current but no difference in resting membrane potential? To complicate the matter even more, neurons *in-vivo* are in high conductance states in awake animals [@destexheHighconductanceStateNeocortical2003]. Some neurons have up and downstates like MSNs. High conductance states mean the neuron has low resistance since they are inversely related. Maybe injecting current is a good thing but needs to be put into context and needs to get the cell to its high conductance state which is usually around -60 mV (at least for pyramidal cells).

Another factor to consider is that some cells, such as dopaminergic cells, glutamatergic cells and interneurons in the VTA spontaneously spike in slices, even with high Mg+ (2 mM) and even after the high K+ solution perfuses the cell in whole cell setup. To test rheobase you have to inject some current so you will likely need to at least hold them below the spike threshold. I have read that you cannot actually test rheobase in these cells because they are spontaneously firing. Instead you can see how much current it takes to suppress the spontaneous firing. On the other hand, many internals used for current clamp experiments primarily composed of K+ which I have found hyperpolarizes the cell upon break in so they cease spontaneously spiking.

### Steps vs ramps
As mentioned in the beginning, you can record current steps or ramps. Current steps are the most common. Usually there are negative and positive steps. The negative steps can go as low as -150 to -200 pA and positive currents can as high as 600 pA (some interneurons have a very high rheobase), Steps can be irregular or regularly spaced. One problem with ramps is that some cells have depolarization block and may not spike during a ramp but will during a set of stepped pulses. Depolarization block is the inactivation of voltage-gated sodium channels due to long membrane depolarizations that does not elicit any spikes. There are conditions, such as epilepsy, where depolarization block may actually be an important feature of the cell physiology and you could use the ramp to test whether this occurs. Below you can see and example current injection cycle and a ramp. 
```{image} ../data/current_injections.png
:alt: Electrophysiology current injections
:align: center
```
How do you decide on the length of a current injection? You can do short 3 ms long pulses or long 1000-3000 ms long pulses. You can use short and steep ramps or slow and long ramps. You can run all of these and compare each. However, most commonly you will find that labs use a 500-1000 ms current injection. This is considered infinitely long. The reason has to do with rheobase and a related feature call chronaxie. Short steps are used for different features than long steps. Short steps tend to elicit only a single action potential and can have a different shape compared to long steps with multiple action potentials. You may also notice that in some cells the membrane potential slowly increases after the initial current injection, in a long pulse, until the cell spikes. Other cells, particularly PV interneurons, do not have an increase in membrane potential before spiking. Some features such as membrane tau and voltage sag can only be determined with steps where as others like membrane resistance and rheobase can be determined from ramps and steps. You should have several seconds between currents steps since some neurons have a prolonged mild hyperpolarization that can last several seconds with positive current injections. 

Lastly you should consider whether or not you want to run multiple cycles of the pulses. Some labs only run one cycle with small steps to save time. Other labs run several cycles/epochs and average the values from each of the cycles/epochs. One thing I will point out is that neurons are probablistic and priors can change how a neurons is likely to function. Some would argument that a cycle of current injections will alter the function of a neuron. However, the internal we use tends to hyperpolarize cells and we put in Ca+ chelator's like EGTA. Others will argue that because neurons are probablistic you need to to run several cycles to get the central tendency of a particular characteristic (like rheobase) of a cell.

### Noise injections
You can add noise to your current injections to simulate the noisy synaptic inputs that cells would receive *in vivo*. Noise is typically pink noise or white noise. White noise is noise with equal power across the frequency spectrum. Pink noise is noise whose frequency spectrum follows the $1/f$ power distribution. Compared to white noise, you can see that the mean "moves" with time in the pink noise. Noise injections are particularly useful when fitting computational models since noise injections take into account the nonlinear resistive properties of neurons. Noise is generally scaled to 10-20% of the amplitude of the current injection you are running or by setting the noise amplitude to 0.2 coefficient of variation. You will also want to freeze the noise using a seed for a random number generator (provide you use the same random number generator) so that every neuron gets the same noise sequence. Lastly, you can use noise injections to test how reliably a neuron fires if you repeat the noise injection several times. If you are really interested in the nonlinear aspects of neuronal function you should seriously consider using pink noise current injections since they help capture frequency depedent neuron spiking.

#### Example noise current injections
::::{grid} 1 1 2 2
:::{grid-item}
```{figure} ../data/white_noise/white-noise.svg
White noise current injection
```
:::

:::{grid-item}
```{figure} ../data/pink_noise/pink-noise.svg
Pink noise current injection
```
:::
::::
Some other aspects of noise injections are the power and autocorrelation. If you look at the power spectral density of white and pink noise you will see that white noise has equal power across frequencies where pink noise has decreasing power across frequencies. So, $1/f$ means that low frequencies have larger power than high frequencies.

#### Power spectral density of noise
::::{grid} 1 1 2 2
:::{grid-item}
```{figure} ../data/white_noise/white-noise-psd.svg
White noise PSD
```
:::

:::{grid-item}
```{figure} ../data/pink_noise/pink-noise-psd.svg
Pink noise PSD
```
:::
::::
Each noise also has an autocorrelation that is important for the computation aspects of the noise. Pink noise has large correlations at short time scales because low frequencies are predominate so temporal correlation goes up. White has very little correlation structure. For that reason white noise is typically filtered with an exponential kernel. The exponential kernel *tau* correlates the noise by reducing the power of frequencies of high frequencies below the cutoff ($\frac{1}{2\pi \tau}$). It essentially simulates the decay of synaptic input. Long tau means slower fluctuations will predominate creating a peak in the autocorrelation a 0. The benefit of pink noise is that it is multiscale (fluctuation across multiple timescales) where as white noise is totally random with no multiscale fluctuations. Multiscale means that many timescales are represented which means that the signal can have memory or correlation. Multiscale is also more *in-vivo* like since it captures slow state changes like arousal and faster changes like network oscillations and synaptic conductances. The decay in the autocorrelation is because low frequencies are predominately driving how the noise "looks". 

#### Noise autocorrelation
::::{grid} 1 1 2 2
:::{grid-item}
```{figure} ../data/white_noise/white-noise-auto-corr.svg
White noise autocorrelation
```
:::

:::{grid-item}
```{figure} ../data/pink_noise/pink-noise-auto-corr.svg
Pink noise autocorrelation
```
:::
::::

### Chirp
A chirp is a sine wave that changes in frequency over time, usually going from low to high frequency. Chirps are used to test the resonant frequency of a neuron or the nonlinear resistance of neuron. If possible I recommend running chirps since they capture how the capacitance and membrane resistance interact.
```{image} ../data/chirp.svg
:alt: Electrophysiology current injections
:align: center
```