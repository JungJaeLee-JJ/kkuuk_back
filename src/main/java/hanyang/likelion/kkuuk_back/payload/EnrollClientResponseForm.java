package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Client;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EnrollClientResponseForm extends ResponseForm {
  private ClientInfo info;

  public EnrollClientResponseForm(String msg, Client client) {
    super(msg);
    this.info = new ClientInfo(client);
  }
}
