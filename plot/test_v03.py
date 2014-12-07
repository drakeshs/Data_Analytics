#! /usr/bin/env python

# You can reproduce this figure in Python with the following code!

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('Python-Demo-Account', 'gwt101uhh0')
trace1 = Scatter(
    x=[8.2],
    y=[953.8],
    mode='markers',
    name='trace 0',
    text=['State: Obama <br>Population: 4627851'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[21.289863565054436],
        line=Line(
            width=1
        ),
        opacity=0.9,
        sizemode='diameter'
    )
)
trace2 = Scatter(
    x=[4.8],
    y=[622.5],
    mode='markers',
    name='trace 1',
    text=['State: Alaska <br>Population: 686293'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[8.19856754494344],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace3 = Scatter(
    x=[7.5],
    y=[948.4],
    mode='markers',
    name='trace 2',
    text=['State: Arizona <br>Population: 6500180'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[25.231663607496543],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace4 = Scatter(
    x=[6.7],
    y=[1084.6],
    mode='markers',
    name='trace 3',
    text=['State: Arkansas<br>Population: 2855390'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[16.72306629772575],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace5 = Scatter(
    x=[6.9],
    y=[693.3],
    mode='markers',
    name='trace 4',
    text=['State: Lalo <br>Population: 36756666'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[60],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace6 = Scatter(
    x=[3.7],
    y=[744.8],
    mode='markers',
    name='trace 5',
    text=['State: Colorado <br>Population: 4861515'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[21.82071662856562],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace7 = Scatter(
    x=[2.9],
    y=[437.1],
    mode='markers',
    name='trace 6',
    text=['State: Connecticut <br>Population: 3501252'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[18.518034093927596],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace8 = Scatter(
    x=[4.4],
    y=[688.9],
    mode='markers',
    name='trace 7',
    text=['State: Delaware <br>Population: 873092'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[9.247262772622127],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace9 = Scatter(
    x=[5],
    y=[926.3],
    mode='markers',
    name='trace 8',
    text=['State: Florida <br>Population: 18328340'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[42.368663121167216],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace10 = Scatter(
    x=[6.2],
    y=[931],
    mode='markers',
    name='trace 9',
    text=['State: Georgia <br>Population: 9685744'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[30.799927023381183],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace11 = Scatter(
    x=[1.9],
    y=[767.9],
    mode='markers',
    name='trace 10',
    text=['State: Hawaii <br>Population: 1288198'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[11.232450274563602],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace12 = Scatter(
    x=[2.4],
    y=[564.4],
    mode='markers',
    name='trace 11',
    text=['State: Idaho <br>Population: 1523816'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[12.216574817330308],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace13 = Scatter(
    x=[6],
    y=[606.9],
    mode='markers',
    name='trace 12',
    text=['State: Illinois <br>Population: 12901563'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[35.5471149110585],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace14 = Scatter(
    x=[5.7],
    y=[697.6],
    mode='markers',
    name='trace 13',
    text=['State: Indiana <br>Population: 6376792'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[24.99103944778468],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace15 = Scatter(
    x=[1.3],
    y=[606.4],
    mode='markers',
    name='trace 14',
    text=['State: Iowa <br>Population: 3002555'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[17.148600386683828],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace16 = Scatter(
    x=[3.7],
    y=[689.2],
    mode='markers',
    name='trace 15',
    text=['State: Kansas  <br>Population: 2802134'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[16.56638096342029],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace17 = Scatter(
    x=[4.6],
    y=[634],
    mode='markers',
    name='trace 16',
    text=['State: Kentucky  <br>Population: 4269245'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[20.44837182682112],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace18 = Scatter(
    x=[9.9],
    y=[870.6],
    mode='markers',
    name='trace 17',
    text=['State: Louisiana <br>Population: 4410796'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[20.784600454895454],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace19 = Scatter(
    x=[1.4],
    y=[478.5],
    mode='markers',
    name='trace 18',
    text=['State: Maine <br>Population: 1316456'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[11.35497986651013],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace20 = Scatter(
    x=[9.9],
    y=[641.4],
    mode='markers',
    name='trace 19',
    text=['State: Maryland <br>Population: 5633597'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[23.489624950340385],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace21 = Scatter(
    x=[2.7],
    y=[541.1],
    mode='markers',
    name='trace 20',
    text=['State: Massachusetts<br>Population: 6497967'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[25.22736815530246],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace22 = Scatter(
    x=[6.1],
    y=[696.8],
    mode='markers',
    name='trace 21',
    text=['State: Michigan<br>Population: 10003422'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[31.300947885457816],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace23 = Scatter(
    x=[2.2],
    y=[578.9],
    mode='markers',
    name='trace 22',
    text=['State: Minnesota <br>Population: 5220393'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[22.611782205315848],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace24 = Scatter(
    x=[7.3],
    y=[919.7],
    mode='markers',
    name='trace 23',
    text=['State: Mississippi <br>Population: 2938618'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[16.965035065108452],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace25 = Scatter(
    x=[6.9],
    y=[738.3],
    mode='markers',
    name='trace 24',
    text=['State: Missouri <br>Population: 5911605'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[24.062231362162844],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace26 = Scatter(
    x=[1.9],
    y=[389.2],
    mode='markers',
    name='trace 25',
    text=['State: Montana  <br>Population: 967440'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[9.734086794334726],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace27 = Scatter(
    x=[2.5],
    y=[532.4],
    mode='markers',
    name='trace 26',
    text=['State: Nebraska <br>Population: 1783432'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[13.216348191564299],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace28 = Scatter(
    x=[8.5],
    y=[972.4],
    mode='markers',
    name='trace 27',
    text=['State: Nevada <br>Population: 2600167'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[15.958196758891171],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace29 = Scatter(
    x=[1.4],
    y=[317],
    mode='markers',
    name='trace 28',
    text=['State: New Hampshire <br>Population: 1315809'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[11.35218920170073],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace30 = Scatter(
    x=[4.8],
    y=[447.1],
    mode='markers',
    name='trace 29',
    text=['State: New Jersey<br>Population: 8682661'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[29.161483723458186],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace31 = Scatter(
    x=[7.4],
    y=[1093.9],
    mode='markers',
    name='trace 30',
    text=['State: New Mexico <br>Population: 1984356'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[13.9409698748354],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace32 = Scatter(
    x=[4.5],
    y=[353.3],
    mode='markers',
    name='trace 31',
    text=['State: New York<br>Population: 19490297'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[43.69104406234709],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace33 = Scatter(
    x=[6.7],
    y=[1201.1],
    mode='markers',
    name='trace 32',
    text=['State: North Carolina <br>Population: 9222414'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[30.054222786572133],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace34 = Scatter(
    x=[1.1],
    y=[311.9],
    mode='markers',
    name='trace 33',
    text=['State: North Dakota <br>Population: 641481'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[7.926383724761497],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace35 = Scatter(
    x=[5.1],
    y=[872.8],
    mode='markers',
    name='trace 34',
    text=['State: Ohio <br>Population: 11485910'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[33.540219377041865],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace36 = Scatter(
    x=[5.3],
    y=[1006],
    mode='markers',
    name='trace 35',
    text=['State: Oklahoma <br>Population: 3642361'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[18.887509160783615],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace37 = Scatter(
    x=[2.2],
    y=[758.6],
    mode='markers',
    name='trace 36',
    text=['State: Oregon <br>Population: 3790060'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[19.26665128765502],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace38 = Scatter(
    x=[6.1],
    y=[451.6],
    mode='markers',
    name='trace 37',
    text=['State: Pennsylvania<br>Population: 12448279'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[34.9170746290055],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace39 = Scatter(
    x=[3.2],
    y=[494.2],
    mode='markers',
    name='trace 38',
    text=['State: Rhode Island <br>Population: 1050788'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[10.144735928158315],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace40 = Scatter(
    x=[7.4],
    y=[1000.9],
    mode='markers',
    name='trace 39',
    text=['State: South Carolina <br>Population: 4479800'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[20.946550209950495],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace41 = Scatter(
    x=[2.3],
    y=[324.4],
    mode='markers',
    name='trace 40',
    text=['State: South Dakota <br>Population: 804194'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[8.874902869774182],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace42 = Scatter(
    x=[7.2],
    y=[1026.9],
    mode='markers',
    name='trace 41',
    text=['State: Tennessee <br>Population: 6214888'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[24.671743864031427],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace43 = Scatter(
    x=[6.2],
    y=[961.6],
    mode='markers',
    name='trace 42',
    text=['State: Texas <br>Population: 24326974'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[48.812071626744064],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace44 = Scatter(
    x=[2.3],
    y=[606.2],
    mode='markers',
    name='trace 43',
    text=['State: Utah<br>Population: 2736424'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[16.370987985723886],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace45 = Scatter(
    x=[1.3],
    y=[491.8],
    mode='markers',
    name='trace 44',
    text=['State: Vermont <br>Population: 621270'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[7.800516966644794],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace46 = Scatter(
    x=[6.1],
    y=[392.1],
    mode='markers',
    name='trace 45',
    text=['State: Virginia <br>Population: 7769089'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[27.584698576472263],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace47 = Scatter(
    x=[3.3],
    y=[959.7],
    mode='markers',
    name='trace 46',
    text=['State: Washington <br>Population: 6549224'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[25.32667146154316],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace48 = Scatter(
    x=[4.4],
    y=[621.2],
    mode='markers',
    name='trace 47',
    text=['State: West Virginia <br>Population: 1814468'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[13.33085028717251],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace49 = Scatter(
    x=[3.5],
    y=[440.8],
    mode='markers',
    name='trace 48',
    text=['State: Wisconsin <br>Population: 5627967'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[23.477884702899185],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
trace50 = Scatter(
    x=[2.7],
    y=[476.3],
    mode='markers',
    name='trace 49',
    text=['State: Wyoming <br>Population: 532668'],
    marker=Marker(
        color='rgba(43, 124, 205, 0.5)',
        size=[7.222898268890642],
        line=Line(
            width=1
        ),
        opacity=0.9
    )
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20, trace21, trace22, trace23, trace24, trace25, trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33, trace34, trace35, trace36, trace37, trace38, trace39, trace40, trace41, trace42, trace43, trace44, trace45, trace46, trace47, trace48, trace49, trace50])
layout = Layout(
    title='US Crime Rate by State',
    titlefont=Font(
        family='',
        size=20,
        color=''
    ),
    font=Font(
        family='"PT Sans Narrow", sans-serif',
        size=14,
        color='#000'
    ),
    showlegend=False,
    autosize=False,
    width=600,
    height=500,
    xaxis=XAxis(
        title='Number of Murders per 100,000 people',
        titlefont=Font(
            family='',
            size=0,
            color=''
        ),
        range=[0.46977371991753625, 10.757659298492284],
        domain=[0, 1],
        type='linear',
        rangemode='normal',
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        nticks=12,
        ticks='',
        showticklabels=True,
        tick0=0,
        dtick=1,
        ticklen=5,
        tickwidth=1,
        tickcolor='#000',
        tickangle='auto',
        tickfont=Font(
            family='',
            size=0,
            color=''
        ),
        exponentformat='e',
        showexponent='all',
        mirror='all',
        gridcolor='#ddd',
        gridwidth=1,
        zerolinecolor='#000',
        zerolinewidth=1,
        linecolor='white',
        linewidth=1,
        anchor='y',
        overlaying=False,
        position=0
    ),
    yaxis=YAxis(
        title='Number of Burglaries per 100,000 people',
        titlefont=Font(
            family='',
            size=0,
            color=''
        ),
        range=[201.5257362471584, 1323.0043355814962],
        domain=[0, 1],
        type='linear',
        rangemode='normal',
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        nticks=12,
        ticks='',
        showticklabels=True,
        tick0=0,
        dtick=100,
        ticklen=5,
        tickwidth=1,
        tickcolor='#000',
        tickangle='auto',
        tickfont=Font(
            family='',
            size=0,
            color=''
        ),
        exponentformat='e',
        showexponent='all',
        mirror='all',
        gridcolor='#ddd',
        gridwidth=1,
        zerolinecolor='#000',
        zerolinewidth=1,
        linecolor='white',
        linewidth=1,
        anchor='x',
        overlaying=False,
        position=0
    ),
    legend=Legend(
        traceorder='normal',
        font=Font(
            family='',
            size=0,
            color=''
        ),
        bgcolor='#fff',
        bordercolor='#000',
        borderwidth=1
    ),
    margin=Margin(
        l=80,
        r=80,
        b=80,
        t=100,
        pad=2
    ),
    paper_bgcolor='rgb(245, 245, 245)',
    plot_bgcolor='rgb(245, 245, 245)',
    hovermode='closest',
    dragmode='zoom',
    separators='.,',
    barmode='stack',
    bargap=0.2,
    bargroupgap=0,
    boxmode='overlay',
    boxgap=0.3,
    boxgroupgap=0.3
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
