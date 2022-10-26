% import igra_tipkanje
% rebase('osnovna_stran.tpl')

<nav class="level">
    <div class="box center">
    <div class="columns">
            <div class="column is-half">
                Vpišite naslednje besedilo:
            </div>
            <div class="column is-half has-text-right" style="color:gray; font-size:11px">
                {{trenutni_indeks}}/{{st_indeksov}}
            </div>
        </div>
        <div class="panel-block">
            <h1>{{trenutno_besedilo}}</h1>
        </div>
        <form autocomplete="off" action="/preveri-besedilo" method="POST">
            Vnos: <input type = "text" class="input is-big is rounded" autofocus name="besedilo">
            <input type="submit" class="button-is-info button2" value="Vpiši">
        </form>
    </div>
</nav>
