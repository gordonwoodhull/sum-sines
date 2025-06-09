import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Sum of Sines in Marimo

    The Altair chart below shows the sum of two sine waves.

    You can adjust the parameters here:
    """
    )
    return


@app.cell
def _(mo):
    amp1 = mo.ui.slider(0, 5, value=0.5, step=0.01, label="amplitude 1")
    freq1 = mo.ui.slider(0, 100, value=1, label="frequency 1")
    ofs1 = mo.ui.slider(0, 1, value=0, step=0.01, label="offset 1")

    amp2 = mo.ui.slider(0, 5, value=0.5, step=0.01, label="amplitude 2")
    freq2 = mo.ui.slider(0, 100, value=1, label="frequency 2")
    ofs2 = mo.ui.slider(0, 1, value=0, step=0.01, label="offset 2")

    mo.md(f"""
    <table>
    <tr>
    <td>
    {amp1}
    {freq1}
    {ofs1}
    </td>
    <td>
    {amp2}
    {freq2}
    {ofs2}
    </td>
    </tr>
    </table>
    """)

    return amp1, amp2, freq1, freq2, ofs1, ofs2


@app.cell
def _(amp1, amp2, freq1, freq2, ofs1, ofs2):
    # Create sine wave with Altair
    import altair as alt
    import numpy as np
    import pandas as pd

    # Create data for a sine wave
    x = np.linspace(0, 1, 300)
    y1 = amp1.value * np.sin((x + ofs1.value)*freq1.value*2*np.pi)
    y2 = amp2.value * np.sin((x + ofs2.value)*freq2.value*2*np.pi)
    sine_data = pd.DataFrame({'x': x, 'y': y1 + y2})

    # Create the sine wave plot with Altair
    sine_chart = alt.Chart(sine_data).mark_line(
        color='blue', 
        strokeWidth=2
    ).add_params(
        alt.selection_interval(bind='scales')  # Makes chart zoomable/pannable
    ).encode(
        x=alt.X('x:Q', title='x (radians)'),
        y=alt.Y('y:Q', title='sin(x)')
    ).properties(
        title='Sum of Sine Waves',
        width=500,
        height=300
    ).interactive()

    sine_chart
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
