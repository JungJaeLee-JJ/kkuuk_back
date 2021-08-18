package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EnrollClientRequestForm {
  private Long storeId;
  private String username;
  private String last4digit;
}
