package hanyang.likelion.kkuuk_back.payload;

import hanyang.likelion.kkuuk_back.model.Store;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class StoreInfo {
  private Long id;
  private String name;

  public StoreInfo(Long id, String name) {
    this.id = id;
    this.name = name;
  }

  public static StoreInfo of(Store store){
    return new StoreInfo(store.getId(),store.getName());
  }
}
