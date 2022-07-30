"""
sss
"""

from ..packages import *
from ..styles.style import url_theme1, url_theme2


def generic_graph():
    fig = go.Figure()
    draft_template = go.layout.Template()
    draft_template.layout.annotations = [
        dict(
            name='draft watermark',
            text='DRAFT',
            textangle=-10,
            opacity=0.1,
            font=dict(color='black', size=40),
            xref='paper',
            yref='paper',
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
    return fig, draft_template


def graph_no_data(parametro, forma_abastecimento_nome):
    fig, draft_template = generic_graph()
    fig.update_layout(
        template=draft_template,
        annotations=[
            dict(
                templateitemname='draft watermark',
                text=f'Não tem<br>Amostras de<br>{parametro}<br>para {forma_abastecimento_nome}',
            )
        ]
    )
    return fig


def graph_error_query(parametro, forma_abastecimento_nome):
    fig, draft_template = generic_graph()
    fig.update_layout(
        template=draft_template,
        annotations=[
            dict(
                templateitemname='draft watermark',
                text=f'Query Inválida<br>{parametro}<br>para {forma_abastecimento_nome}',
            )
        ]
    )
    return fig


def graph_vig_basic(x, y, parametro, forma_abastecimento_nome):
    fig = go.Figure()
    templates = [
        'bootstrap',
        'minty',
        'pulse',
        'flatly',
        'quartz',
        'cyborg',
        'darkly',
        'vapor',
    ]
    load_figure_template(templates)

    # Add trace
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            name='conclusao',
            mode='markers',
            marker={'color': 'blue'},
            opacity=0.8,
        )
    )

    # Update
    print(parametro)
    fig.update_layout(
        title=f'{" ".join(parametro)}<br><sup>{forma_abastecimento_nome}</sup>',
        xaxis_tickformat='%d %b<br>%Y',
        margin={
            'l': 40,
            'b': 40,
            # 't': 40,
            'r': 0
        },
        # dragmode='pan',
        hovermode='x',
        template=templates[0],
    )
    return fig





