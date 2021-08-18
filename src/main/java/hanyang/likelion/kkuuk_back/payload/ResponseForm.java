package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ResponseForm {

  private String msg;

  public ResponseForm(String msg) {
    this.msg = msg;
  }
}
