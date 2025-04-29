template_psc_callback = """
    if (rise_tau === decay_tau) {
        rise_tau += 0.001;
    }
    const s_r_c = 10
    const rt = Math.round(rise_tau.value * s_r_c)
    const dt = Math.round(decay_tau.value * s_r_c)
    const len = Math.round(length.value * s_r_c)
    const spacer = 15
    const y = new Array(len+spacer).fill(0)
    const t_length = Array.from({ length: len }, (_, i) => 0 + i)
    const Aprime = (dt / rt) ** (rt / (rt - dt))
    const temp_y = t_length.map(x => {
        return amplitude.value / Aprime * ((1 - Math.exp(-x / rt)) ** risepower.value * Math.exp(-x / dt))
    })
    y.splice(spacer, temp_y.length, ...temp_y);
    const x = Array.from({ length: len+spacer }, (_, i) => 0 + i/10)
    source.data = { x, y }
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