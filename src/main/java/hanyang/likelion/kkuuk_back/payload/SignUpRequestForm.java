package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class SignUpRequestForm {
  private String email;
  private String password;
  private String call;
  private String name;
}
