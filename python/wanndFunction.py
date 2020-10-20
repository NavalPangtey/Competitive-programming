from wand.image import image

frequency = 3
phase_shift = -90
amplitude = 0.2
bias = 0.7

with Image(filename ="koala.jpeg") as img:
    # appying sinusoid FUCTION_TYPE
    img.function('sinusoid', [frequency, phase_shift, amplitude, bias])
    img.save(filename ="kl-functioned.jpeg")
