# Tool to visualize color palettes in an HTML file

def stylesheet():
    """
    Print out a short CSS stylesheet that gives color chips
    rounded corners and that pop out when hovered over
    """
    print("""\
<style>
    .container {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        height: 95%;
    }

    div > div {
        background-color: #f1f1f1;
        border-radius: 15px;
        font-family: monospace;
        font-size: 10pt;
        height: 50px;
        line-height: 50px;
        padding: 0 25px;
        transform: none;
        transition-duration: 150ms;
        transition-property: transform;
        transition-timing-function: ease-in-out;
    }

    div > div:hover {
        transform: scale(1.5);
    }

    div > span {
        border-radius: 15%;
        float: left;
        height: 50px;
        margin: 0 5px 0 -30px;
        width: 50px;
    }
</style>""")


def html_palette(name, colors):
    """
    Given the name of a color palette's and a list of strings representing colors,
    print HTML for a flexbox <div> that is nearly as tall as the screen containing
    color chips beside their hex RGB value.  Scroll sideways to take in the
    whole palette.
    """
    print(f"""<h2>{name} ({len(colors)} colors {colors[0]}->{colors[-1]})</h2>\n<div class="container">""")
    for color in colors:
        print(f"""    <div><span style="background-color: {color}"> </span>{color}</div>""")
    print("</div>")

# :autocmd bufwritepost <buffer> silent !python3 palette.py > palette.html

