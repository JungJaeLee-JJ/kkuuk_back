package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ClientsByUsernameRequestForm {
  private Long storeId;
  private String username;
}
