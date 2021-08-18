package hanyang.likelion.kkuuk_back.exception;

import hanyang.likelion.kkuuk_back.payload.ResponseForm;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class ExceptionResponseForm extends ResponseForm {
  private String path;

  public ExceptionResponseForm(String msg, String path) {
    super(msg);
    this.path = path;
  }
}
