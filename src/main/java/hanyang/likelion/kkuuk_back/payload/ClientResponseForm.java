package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Client;
import java.util.List;
import java.util.stream.Collectors;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ClientResponseForm {

  private List<ClientInfo> infos;

  public ClientResponseForm(List<ClientInfo> infos) {
    this.infos = infos;
  }

  public static ClientResponseForm of(List<Client> clientList) {
    return new ClientResponseForm(clientList.stream().map(ClientInfo::new).collect(Collectors.toList()));
  }
}
