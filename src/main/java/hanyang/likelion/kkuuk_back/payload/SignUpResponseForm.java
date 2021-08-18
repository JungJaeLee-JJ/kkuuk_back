package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Store;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class SignUpResponseForm extends ResponseForm {
  private StoreInfo info;

  public SignUpResponseForm(String msg, Store store) {
    super(msg);
    StoreInfo info = StoreInfo.of(store);
    this.info = info;
  }

  public static SignUpResponseForm of(String msg, Store store){
    return new SignUpResponseForm(msg,store);
  }
}
