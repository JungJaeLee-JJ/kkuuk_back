package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Client;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ClientInfo {

  private Long id;
  private String name;
  private String last4digit;
  private Long stamp;

  public ClientInfo(Client client) {
    this.id = client.getId();
    this.name = client.getName();
    this.last4digit = client.getLast4Digit();
    this.stamp = client.getStamp();
  }
}
