function onload()
{
    dragElement( document.getElementById("separator"), "H" );

}



// This function is used for dragging and moving
function dragElement( element, direction, handler )
{
  // Two variables for tracking positions of the cursor
  const drag = { x : 0, y : 0 };
  const delta = { x : 0, y : 0 };
  /* If present, the handler is where you move the DIV from
     otherwise, move the DIV from anywhere inside the DIV */
  handler ? ( handler.onmousedown = dragMouseDown ): ( element.onmousedown = dragMouseDown );

  // A function that will be called whenever the down event of the mouse is raised
  function dragMouseDown( e )
  {
    drag.x = e.clientX;
    drag.y = e.clientY;
    document.onmousemove = onMouseMove;
    document.onmouseup = () => { document.onmousemove = document.onmouseup = null; }
  }

  // A function that will be called whenever the up event of the mouse is raised
  function onMouseMove( e )
  {
    const currentX = e.clientX;
    const currentY = e.clientY;

    delta.x = currentX - drag.x;
    delta.y = currentY - drag.y;

    const offsetLeft = element.offsetLeft;
    const offsetTop = element.offsetTop;


    const first = document.getElementById("sidebar");
    const second = document.getElementById("note");
    let firstWidth = first.offsetWidth;
    let secondWidth = second.offsetWidth;
    if (direction === "H" ) // Horizontal
    {
        element.style.left = offsetLeft + delta.x + "px";
        firstWidth += delta.x;
        secondWidth -= delta.x;
    }
    drag.x = currentX;
    drag.y = currentY;
    first.style.width = firstWidth + "px";
    second.style.width = secondWidth + "px";
  }
}


function collapse(){
    const sidebar = document.getElementById("sidebar");
    const note = document.getElementById("note");
    const menu_visible = document.getElementById("menu-visible");
    const menu_invisible = document.getElementById("menu-invisible");

    if (sidebar.style.display !== 'none') {
        sidebar.style.display = 'none';
        note.style.minWidth = "99%";
        note.style.maxWidth = "99%";
        menu_invisible.style.display = 'none';
        menu_visible.style.display = 'inherit';
    }
    else {
        sidebar.style.display = 'block';
        note.style.minWidth = "50vw";
        note.style.maxWidth = "100vw";
        menu_invisible.style.display = 'inherit';
        menu_visible.style.display = 'none';
    }

}