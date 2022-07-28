#!/usr/bin/env python
# coding: utf-8



import plotly.graph_objects as go




def graph_no_data(parametro, forma_abastecimento_nome):
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
    fig.update_layout(
        template=draft_template,
        annotations=[
            dict(
                templateitemname='draft watermark',
                text='Não tem<br>Amostras de<br>{}<br>para {}'.format(parametro, forma_abastecimento_nome),
            )
        ]
    )
    return fig









def graph_error_query(parametro, forma_abastecimento_nome):
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
    fig.update_layout(
        template=draft_template,
        annotations=[
            dict(
                templateitemname='draft watermark',
                text='Query Inválida<br>{}<br>para {}'.format(parametro, forma_abastecimento_nome),
            )
        ]
    )
    return fig







def graph_vig_basic(x, y, parametro, forma_abastecimento_nome):
    fig = go.Figure()

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
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(parametro), forma_abastecimento_nome),
        xaxis_tickformat='%d %b<br>%Y',
        margin={
            'l': 40,
            'b': 40,
            # 't': 40,
            'r': 0
        },
        # dragmode='pan',
        hovermode='x',
    )
    return fig
