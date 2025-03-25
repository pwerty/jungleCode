from pyflowchart import Flowchart
from pyflowchart import output_html 
with open('boj2630.py') as f:
    code = f.read()

    fc = Flowchart.from_code(code)
    print(fc.flowchart())
    output_html('output.html', 'a_pyflow_test', fc.flowchart())