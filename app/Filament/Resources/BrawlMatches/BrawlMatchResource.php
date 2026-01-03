<?php

namespace App\Filament\Resources\BrawlMatches;

use App\Filament\Resources\BrawlMatches\Pages\CreateBrawlMatch;
use App\Filament\Resources\BrawlMatches\Pages\EditBrawlMatch;
use App\Filament\Resources\BrawlMatches\Pages\ListBrawlMatches;
use App\Filament\Resources\BrawlMatches\Schemas\BrawlMatchForm;
use App\Filament\Resources\BrawlMatches\Tables\BrawlMatchesTable;
use App\Models\BrawlMatch;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;

class BrawlMatchResource extends Resource
{
    protected static ?string $model = BrawlMatch::class;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedRectangleStack;

    protected static ?string $recordTitleAttribute = 'tournament_name';

    public static function form(Schema $schema): Schema
    {
        return BrawlMatchForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return BrawlMatchesTable::configure($table);
    }

    public static function getRelations(): array
    {
        return [
            //
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListBrawlMatches::route('/'),
            'create' => CreateBrawlMatch::route('/create'),
            'edit' => EditBrawlMatch::route('/{record}/edit'),
        ];
    }
}
