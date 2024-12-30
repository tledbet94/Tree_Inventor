from dash import dcc, html
import dash_bootstrap_components as dbc

# Table cells (TDs)
node_label = html.Td('Label', id='info-label', className='info-text-label',
                     style={'backgroundColor': '#868188'})
node_name = html.Td(id='node-name', className='info-text-actual',
                    style={'backgroundColor': '#868188'})

weight_label = html.Td('Weight', id='info-weight', className='info-text-label',
                       style={'backgroundColor': '#4B80CA'})
weight_actual = html.Td(id='node-weight', className='info-text-actual',
                        style={'backgroundColor': '#4B80CA'})

level_label = html.Td('Level', id='info-level', className='info-text-label',
                      style={'backgroundColor': '#D3A068'})
level_actual = html.Td(id='node-level', className='info-text-actual',
                       style={'backgroundColor': '#D3A068'})

custom1_label = html.Td('Custom 1', id='info-custom1-label', className='info-text-label',
                        style={'backgroundColor': '#B45252'})
custom1_actual = html.Td(id='node-custom1', className='info-text-actual',
                         style={'backgroundColor': '#B45252'})

custom2_label = html.Td('Custom 2', id='info-custom2-label', className='info-text-label',
                        style={'backgroundColor': '#4B4158'})

custom2_actual = html.Td(id='node-custom2', className='info-text-actual',
                         style={'backgroundColor': '#4B4158'})

custom3_label = html.Td('Custom 3', id='info-custom3-label', className='info-text-label',
                        style={'backgroundColor': '#567B79'})
custom3_actual = html.Td(id='node-custom3', className='info-text-actual',
                         style={'backgroundColor': '#567B79'})

# Two table rows
row_1 = html.Tr([
    node_label, weight_label,
    level_label, custom1_label,
    custom2_label, custom3_label
])

row_2 = html.Tr([
    node_name, weight_actual,
    level_actual, custom1_actual,
    custom2_actual, custom3_actual
])

# Create the table (no thead, just a tbody)
info_table = dbc.Table(
    html.Tbody([
        row_1,
        row_2,
    ]),
    bordered=True,
    hover=True,
    className='tight-table',
    style={
        'width': 'auto',  # Table width auto
        'tableLayout': 'auto',  # Let columns size based on content
        'marginLeft': 'auto',  # Center horizontally
        'marginRight': 'auto',
        'textAlign': 'center'
        # 'whiteSpace': 'nowrap',   # Uncomment if you want text to never wrap
    }
)

info_contents = dbc.Container(
    [
        dcc.Store(id='info-panel-data'),
        info_table
    ],
    fluid=True,
    className='info-div'
)
