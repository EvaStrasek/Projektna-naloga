% import igra_tipkanje
% rebase('osnovna_stran.tpl')
<nav>
  <div class="box center">
    <div class="mb-4" style="font-weight:bold">
      Igre je konec!
    </div>
    <div class="mb-4">
      Čas: {{cas}} 
    </div>
    <div class="mb-4">
      Število napak: {{st_napak}}
    </div>
    <div class="mb-4">
      Povprečno število napisanih besed na minuto (wpm): {{wpm}}
    </div>
    <table class="table is-hoverable is-fullwidth">
            <tr>
                <th></th>
                <th>Ime</th>
                <th>Čas</th>
                <th>wpm</th>
                <th>Št. napak</th>
            </tr>
            % for rekord in novi_rekordi:
                <tr>
                    <td>{{rekord['ZaporednoMesto']}}</td>
                    <td>{{rekord['Ime']}}</td>
                    <td>{{rekord['Cas']}}</td>
                    <td>{{rekord['Wpm']}}</td>
                    <td>{{rekord['St_napak']}}</td>
                </tr>
            % end
        </table>
  </div>
  

  
</nav>