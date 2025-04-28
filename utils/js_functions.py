template_psc_callback = """
    if rise_tau == decay_tau:
        let rise_tau += 0.001
    let s_r_c = sample_rate / 1000
    let rt = Math.round(rise_tau.value * s_r_c)
    let dt = Math.round(decay_tau.value * s_r_c)
    len = Math.round(length.value * s_r_c)
    let spacer = Math.round(spacer.value * s_r_c)
    let template = np.zeros(len + spacer)
    let t_length = new Array(arraySize).fill(0);
    let offset = len(template) - length
    Aprime = (td / rt) ** (rt / (rt - td))
    let y = Array.from(x, (t_length) => (
        amplitude
        / Aprime
        * ((1 - (Math.exp(-x / rt))) ** risepower * Math.exp((-x / td)))
    )
    template[offset:] = y
"""

view_data = """
    let val = spinner.value
    let URL = `https://raw.githubusercontent.com/LarsHenrikNelson/clampsuite-data/refs/heads/main/${val}.json`
    fetch(URL)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        source.data.y = data["array"].slice(0,100000);
        source.change.emit();
    })
    .catch(error => console.error('Error fetching data:', error));
"""