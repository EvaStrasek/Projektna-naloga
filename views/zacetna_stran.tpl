% import tekstovni_vmesnik
% import igra_tipkanje
% rebase('osnovna_stran.tpl')
<nav class="level">
  <div>
    <form action="/nova-igra" method="POST">
      <div>Izberite si poljubno težavnost igre nato pa za začetek igre kliknite gumb Start</div>
      <div>
          Težavnost
          <select name="tezavnost" id="tezavnost">
            %for tezavnost in tezavnosti:
            <option value="{{tezavnost}}">{{tezavnost}}</option>
            %end
      </div>
      <div>
        <input class="button-is-info" type="submit" value="START"></input>
      </div>
    </form>
  </div>
</nav>
