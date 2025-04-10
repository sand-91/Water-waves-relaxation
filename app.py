import gradio as gr

AUDIO_FILE = "ocean_waves.mp3"

def play_water_waves():
    return AUDIO_FILE

with gr.Blocks(title="Relaxing Water Waves") as demo:
    gr.Markdown("Relaxing Water Waves")
    gr.Markdown("Click below to hear soothing water wave sounds!")
    btn = gr.Button("Play Water Waves")
    output = gr.Audio(label="Relaxing Sounds", interactive=False)
    btn.click(fn=play_water_waves, inputs=None, outputs=output)

demo.launch()
