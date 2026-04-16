from data.app import app
from dash import dcc, html


def find_component_by_id(component, target_id):
    if hasattr(component, "id") and component.id == target_id:
        return True

    if hasattr(component, "children"):
        children = component.children

        if isinstance(children, (list, tuple)):
            for child in children:
                if find_component_by_id(child, target_id):
                    return True
        elif children is not None:
            if find_component_by_id(children, target_id):
                return True

    return False


def find_header(component, target_text):
    if isinstance(component, html.H1) and component.children == target_text:
        return True

    if hasattr(component, "children"):
        children = component.children

        if isinstance(children, (list, tuple)):
            for child in children:
                if find_header(child, target_text):
                    return True
        elif children is not None:
            if find_header(children, target_text):
                return True

    return False


def test_header_present():
    assert find_header(app.layout, "Pink Morsel Sales Visualiser")


def test_graph_present():
    assert find_component_by_id(app.layout, "sales-graph")


def test_radio_present():
    assert find_component_by_id(app.layout, "region-filter")