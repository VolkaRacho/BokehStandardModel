from bokeh.plotting import figure, show, output_notebook
from bokeh.models import (
    ColumnDataSource, 
    HoverTool,
    LabelSet, 
    OpenURL, 
    TapTool,
    )

data = {
    'particle': [
        'up', 'down', 'charm', 'strange', 'top', 'bottom', 
        'electron', 'electron neutrino', 'muon', 'muon neutrino', 
        'tauon', 'tau neutrino', 
        'photon', 'gluon', 'W boson', 'Z boson', 'Higgs'
    ],
    'shorts': [
        'u','d','c','s','t','b',
        'e','ν','μ','ν','τ','ν',
        'ɣ','g','W','Z','H'
    ],
    'color': [
        'red','red','red','red','red','red',
        'blue','blue','blue','blue','blue','blue',
        'yellow','yellow','yellow','yellow','green'
    ],
    'x1': [
        1.05, 1.05, 2.05, 2.05, 3.05, 3.05, 
        1.05, 1.05, 2.05, 2.05, 3.05, 3.05, 
        4.3, 4.3, 4.3, 4.3, 5.4
    ],
    'x2': [
        1.95, 1.95, 2.95, 2.95, 3.95, 3.95, 
        1.95, 1.95, 2.95, 2.95, 3.95, 3.95, 
        5.2, 5.2, 5.2, 5.2, 6.3
    ],
    'y1': [
        3.05, 2.05, 3.05, 2.05, 3.05, 2.05, 
        1.05, 0.05, 1.05, 0.05, 1.05, 0.05, 
        3.05, 2.05, 1.05, 0.05, 3.05
    ],
    'y2': [
        3.95, 2.95, 3.95, 2.95, 3.95, 2.95, 
        1.95, 0.95, 1.95, 0.95, 1.95, 0.95, 
        3.95, 2.95, 1.95, 0.95, 3.95
    ],
    'charge': [
        '2/3','1/3','2/3','1/3','2/3','1/3',
        '1','0','1','0','1','0',
        '0','0','1','0','0'
    ],
    'mass': [
        '2.3 MeV','4.8 MeV','1.3 GeV','95 MeV','173 GeV','4.2 GeV',
        '511 keV','<2 eV','106 MeV','<190 keV','1.8 GeV','<18 MeV',
        '0','0','91 GeV','80 GeV','125 GeV'
    ],
    'spin': [
        '1/2','1/2','1/2','1/2','1/2','1/2',
        '1/2','1/2','1/2','1/2','1/2','1/2',
        '1','1','1','1','0'
    ],
    'type': [
        'quark','quark','quark','quark','quark','quark',
        'lepton','lepton','lepton','lepton','lepton','lepton',
        'gauge boson','gauge boson','gauge boson','gauge boson','boson'
    ],
    'url': [
        'light-quarks','light-quarks','c-quark','light-quarks',
        't-quark','b-quark',
        'electron','neutrino-prop','muon','neutrino-prop',
        'tau','neutrino-prop',
        'photon','gluon','w-boson','z-boson','higgs-boson'
    ],
}

index_data = {
    'x1': [1.05, 2.05, 3.05],
    'y1': [0.05, 0.05, 0.05],
    'index': ['e','μ','τ'],
}


source = ColumnDataSource(data=data)
index_source = ColumnDataSource(data=index_data)

p = figure(title='Standard Model of Particle Physics', toolbar_location=None, 
            plot_width=900, plot_height=900, tools="tap")

p.title.text_font_size = '40pt'
p.title.align = 'center'
p.axis.visible = False
p.xgrid.visible = False
p.ygrid.visible = False

p.quad(source=source, 
        name='particle', 
        bottom='y1', 
        top='y2', 
        left='x1', 
        right='x2',
        fill_color='color', 
        hover_fill_color='color',
        nonselection_fill_color='color', 
        alpha=0.5,
        hover_fill_alpha=0.7,
        nonselection_fill_alpha=0.5,
        line_alpha=0.5,
        nonselection_line_alpha=0.5,
        line_color='black',
        hover_line_color='color',
        nonselection_line_color='black')

labels = LabelSet(x='x1', y='y1', text='particle', level='glyph',
                x_offset=5, y_offset=5, source=source, render_mode='canvas')

large_labels = LabelSet(x='x1', y='y1', text='shorts', level='glyph',
                        x_offset=27, y_offset=45, source=source, 
                        render_mode='canvas',text_font_size='40pt')

index_labels = LabelSet(x='x1', y='y1', text='index', level='glyph',
                        x_offset=55, y_offset=45, source=index_source, 
                        render_mode='canvas',text_font_size='20pt')

TOOLTIPS = """
        <div>
        <span style="font-size: 18px; font-weight: bold; color: @color;">@particle</span>
        </div>
        <div>
        <span style="font-size: 15px;">Type: </span>
        <span style="font-size: 15px;">@type</span>
        </div>
        <div>
        <span style="font-size: 15px;">Mass: </span>
        <span style="font-size: 15px;">@mass</span>
        </div>
        <div>
        <span style="font-size: 15px;">Charge: </span>
        <span style="font-size: 15px;">@charge e</span>
        </div>
        <div>
        <span style="font-size: 15px;">Spin: </span>
        <span style="font-size: 15px;">@spin ħ</span>
        </div>
"""

hover = HoverTool(tooltips = TOOLTIPS)

p.add_tools(hover)
p.hover.point_policy = "follow_mouse"

url = "http://pdg.lbl.gov/2018/listings/rpp2018-list-@url.pdf"

taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

p.add_layout(labels)
p.add_layout(large_labels)
p.add_layout(index_labels)

output_notebook()
show(p)
