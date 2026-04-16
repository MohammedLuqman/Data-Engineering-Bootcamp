from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # Use capital 'S'
from app.database import get_db
from app.models import Quote

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.get("/") 
def get_all(db: Session = Depends(get_db)):
    quotes = db.query(Quote).all()
    return quotes 

@router.get("/{quote_id}")  
def get_quote_by_id(quote_id: int, db: Session = Depends(get_db)):
    result = db.query(Quote).filter(Quote.id == quote_id).first()    
    
    if not result:
        raise HTTPException(status_code=404, detail="Quote not found")
        
    return result
@router.get("/author/{author_name}")  
def get_quote_by_author(author_name: str, db: Session = Depends(get_db)):
    result = db.query(Quote).filter(Quote.author == author_name).all()    
    
    if not result:
        raise HTTPException(status_code=404, detail="No quotes found for this author")
        
    return result