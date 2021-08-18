package hanyang.likelion.kkuuk_back.payload;

import javax.persistence.SecondaryTable;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ClientsByLast4DigitRequestForm {

  private Long storeId;
  private String last4digit;

}
