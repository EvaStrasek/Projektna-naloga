% import tekstovni_vmesnik
% import igra_tipkanje
% rebase('osnovna_stran.tpl')
<nav class="level">
  <div class="box center">
    <form action="/nova-igra" method="POST">
      <div class="mb-4">Izberite si poljuben vzdevek in poljubno težavnost igre nato pa za začetek igre kliknite gumb Start</div>
      <div class="mb-4">
        Uporabniško ime:
        <input type="text" name="uporabnisko_ime" value="{{uporabnisko_ime}}"></input>
      </div>
      <div class="mb-4">
          Težavnost:
          <select name="tezavnost" id="tezavnost">
            %for tezavnost in tezavnosti:
            <option value="{{tezavnost}}">{{tezavnost}}</option>
            %end
      </div>
      <div class=" mt-4 center">
        <input class="button-is-info button" type="submit" value="START"></input>
      </div>
    </form>
  </div>
</nav>
