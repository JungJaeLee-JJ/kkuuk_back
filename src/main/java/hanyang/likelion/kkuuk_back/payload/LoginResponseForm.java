package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Store;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class LoginResponseForm extends ResponseForm {
  private StoreInfo storeInfo;
  private String token;

  public LoginResponseForm(String msg, Store store, String token) {
    super(msg);
    this.storeInfo = StoreInfo.of(store);
    this.token = token;
  }
}
