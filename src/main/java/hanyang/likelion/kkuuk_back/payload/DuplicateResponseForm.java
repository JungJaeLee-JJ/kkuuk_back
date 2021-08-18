package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class DuplicateResponseForm extends ResponseForm {

  private Boolean isDuplicated;

  public DuplicateResponseForm(String msg, Boolean isDuplicated) {
    super(msg);
    this.isDuplicated = isDuplicated;
  }

  public static DuplicateResponseForm of(String msg, Boolean isDuplicated){
    return new DuplicateResponseForm(msg, isDuplicated);
  }
}
