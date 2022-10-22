% import igra_tipkanje
% rebase('osnovna_stran.tpl')

<nav class = "level">
    <div class = "box center">
        <div>
            Vpišite naslednje besedilo:
        </div>
        <div class = "panel-block">
            <h1> {{trenutno_besedilo}}</h1>
        </div>
        <form action = "/preveri-besedilo" method = "POST">
            Vnos: <input type = "text" class = "input is-big is rounded" autofocus name ="besedilo">
            <input type = "submit" class = "button is-info" value = "Vpiši">
        </form>
    </div>
</nav>
