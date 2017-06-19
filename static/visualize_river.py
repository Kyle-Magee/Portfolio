from browser import document, timer
from river_sim import Bear, Fish, Ecosystem

# HTML BINDINGS
canvas = document['simBoard']
ctx = canvas.getContext('2d')
# VISUALIZATION PARAMETERS
DEF_COLOR = 'grey'
M_BEAR_COLOR = 'saddlebrown'
F_BEAR_COLOR = 'chocolate'
M_FISH_COLOR = 'steelblue'
F_FISH_COLR = 'turquoise'
REC_SIZE = 75
x_coords = [i * 80 for i in range(10)] * 10
y_coords = sorted([i for i in range(0, 800, 80)] * 10)
coords = list(zip(x_coords, y_coords))


def draw_rects(ecosystem):
    ctx.clearRect(0, 0, 800, 800)
    for i, j in enumerate(coords):
        RECT_COLOR = DEF_COLOR
        ctx.beginPath()
        ctx.rect(j[0], j[1], REC_SIZE, REC_SIZE)
        animal = str(ecosystem[i])
        if 'M.Fish' == animal:
            RECT_COLOR = M_FISH_COLOR
        elif 'F.Fish' == animal:
            RECT_COLOR = F_FISH_COLR
        elif 'M.Bear' == animal:
            RECT_COLOR = M_BEAR_COLOR
        elif 'F.Bear' == animal:
            RECT_COLOR = F_BEAR_COLOR
        ctx.fillStyle = RECT_COLOR
        ctx.fill()
        ctx.strokeStyle = DEF_COLOR
        ctx.stroke()


# SIMULATION PARAMETERS
eco_class = Ecosystem(100)
ecosystem = eco_class


def change_parameters(env):
    form = document['sim_parameters']
    for i in range(int(form.bearcount.value)):
        Bear(ecosystem)
    for i in range(int(form.fishcount.value)):
        Fish(ecosystem)
    timer.set_interval(run_simulation, 1000)


def run_simulation():
    eco_class.time_step()
    draw_rects(ecosystem)


btn = document['update']
btn.bind('click', change_parameters)
